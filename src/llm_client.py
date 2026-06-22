"""多模型可插拔抽象层。

业务代码只调 chat()；用哪个模型由 config.yaml 的 llm: 段决定。
底层用 LiteLLM 统一适配 Anthropic / OpenAI / Gemini / DeepSeek / OpenAI 兼容 / Ollama。
支持主模型失败时按 fallback 列表降级。
"""
from __future__ import annotations

import json as _json

from .config_loader import env, get_config
from .utils import get_logger

log = get_logger()


class LLMUnavailable(RuntimeError):
    """当前 provider 缺少必要的 key/配置。"""


def _provider_params(provider: str, model: str) -> dict:
    """把 (provider, model) 翻译成 LiteLLM 的调用参数（model 前缀 + key/base_url）。"""
    provider = provider.lower()

    if provider == "anthropic":
        key = env("ANTHROPIC_API_KEY")
        if not key:
            raise LLMUnavailable("缺少 ANTHROPIC_API_KEY")
        return {"model": model, "api_key": key}

    if provider == "openai":
        key = env("OPENAI_API_KEY")
        if not key:
            raise LLMUnavailable("缺少 OPENAI_API_KEY")
        return {"model": model, "api_key": key}

    if provider == "gemini":
        key = env("GEMINI_API_KEY")
        if not key:
            raise LLMUnavailable("缺少 GEMINI_API_KEY")
        return {"model": f"gemini/{model}", "api_key": key}

    if provider == "deepseek":
        key = env("DEEPSEEK_API_KEY")
        if not key:
            raise LLMUnavailable("缺少 DEEPSEEK_API_KEY")
        return {"model": f"openai/{model}", "api_key": key,
                "api_base": "https://api.deepseek.com/v1"}

    if provider == "openai_compatible":
        key = env("OPENAI_COMPATIBLE_API_KEY")
        base = env("OPENAI_COMPATIBLE_BASE_URL")
        if not key or not base:
            raise LLMUnavailable("缺少 OPENAI_COMPATIBLE_API_KEY / OPENAI_COMPATIBLE_BASE_URL")
        return {"model": f"openai/{model}", "api_key": key, "api_base": base}

    if provider == "ollama":
        base = env("OLLAMA_BASE_URL") or "http://localhost:11434"
        return {"model": f"ollama/{model}", "api_base": base}

    raise LLMUnavailable(f"未知 provider: {provider}")


def _candidates() -> list[dict]:
    """主模型 + fallback 链。"""
    cfg = get_config().get("llm", {})
    chain = [{"provider": cfg.get("provider", "anthropic"), "model": cfg.get("model")}]
    for fb in cfg.get("fallback") or []:
        chain.append({"provider": fb["provider"], "model": fb["model"]})
    return chain


def available() -> bool:
    """当前配置下是否至少有一个可用 provider（用于无 key 时优雅跳过）。"""
    for cand in _candidates():
        try:
            _provider_params(cand["provider"], cand["model"])
            return True
        except LLMUnavailable:
            continue
    return False


def chat(messages: list[dict], *, system: str | None = None,
         max_tokens: int | None = None, json: bool = False,
         _reasoning_tokens: int = 8000) -> str:
    """统一对话入口。

    json=True 时不依赖 response_format，通过 prompt 要求 + 去围栏 + 修复。
    _reasoning_tokens：额外分配给推理链的 token 预算。
    """
    import litellm

    cfg = get_config().get("llm", {})
    if system:
        messages = [{"role": "system", "content": system}, *messages]

    if json:
        messages = [*messages, {"role": "user",
                     "content": "\n严格只输出合法 JSON。不要 markdown 围栏、不要注释、"
                                "不要在 JSON 前后加任何说明文字。"}]

    last_err: Exception | None = None
    for cand in _candidates():
        try:
            params = _provider_params(cand["provider"], cand["model"])
        except LLMUnavailable as e:
            last_err = e
            continue

        model_name = params.get("model", "")
        is_deepseek = "deepseek" in model_name.lower()
        is_reasoning = is_deepseek or "-r1" in model_name.lower()

        kwargs = params | {
            "messages": messages,
            "temperature": cfg.get("temperature", 0.3),
            "max_tokens": (max_tokens or cfg.get("max_tokens", 4000)),
            # 单次调用超时（秒）：防止进程在网络/休眠等异常下无限挂起。默认 30 分钟。
            "timeout": cfg.get("timeout_seconds", 1800),
        }
        if is_reasoning:
            kwargs["max_tokens"] = kwargs["max_tokens"] + _reasoning_tokens

        try:
            resp = litellm.completion(**kwargs)
            msg = resp["choices"][0]["message"]
            content = msg.get("content") or ""

            # 推理模型有时 content 为空，用 reasoning_content 兜底
            if not content and is_reasoning:
                content = msg.get("reasoning_content") or ""

            if json:
                content = _strip_fences(content)
                # 丢弃推理模型可能在 JSON 前输出的无关文字（如 brief intro）
                content = _find_json_block(content)
            return content
        except Exception as e:
            log.warning("LLM 调用失败（%s/%s）：%s，尝试降级",
                        cand["provider"], cand["model"], e)
            last_err = e
            continue

    raise RuntimeError(f"所有 LLM 候选均不可用：{last_err}")


def chat_json(messages: list[dict], *, system: str | None = None,
              max_tokens: int | None = None, retries: int = 0):
    """要求 JSON 输出并解析。JSON 损坏时自动调一次修复调用。"""
    raw = chat(messages, system=system, max_tokens=max_tokens, json=True,
               _reasoning_tokens=8000)
    parsed = _try_parse_json(raw)
    if isinstance(parsed, dict):
        return parsed

    # JSON 损坏：追加修复提示重试一次
    if retries > 0:
        log.info("JSON 解析失败，请求模型修复…")
        fix_messages = [*messages,
                        {"role": "assistant", "content": raw},
                        {"role": "user", "content": "你的 JSON 无法解析。请严格只输出修正后的合法 JSON。"}]
        raw2 = chat(fix_messages, system=system, max_tokens=max_tokens,
                    json=True, _reasoning_tokens=4000)
        parsed2 = _try_parse_json(raw2)
        if isinstance(parsed2, dict):
            return parsed2

    raise ValueError(f"LLM 未输出合法 JSON：{raw[:300]}")


def _try_parse_json(text: str):
    """尝试解析 JSON，失败返回 None。"""
    try:
        return _json.loads(_strip_fences(text))
    except (_json.JSONDecodeError, ValueError):
        pass
    # 尝试提取最外层 {} 并修复常见问题
    try:
        block = _find_json_block(text)
        # 去掉尾逗号
        import re
        block = re.sub(r",\s*}", "}", block)
        block = re.sub(r",\s*]", "]", block)
        return _json.loads(block)
    except (_json.JSONDecodeError, ValueError):
        pass
    return None


def _find_json_block(text: str) -> str:
    """从文本中抽出**第一个完整且括号配对**的 JSON 块。

    能丢弃前置说明文字（"Here is the JSON:"）和尾部围栏/多余内容；
    括号匹配时会跳过字符串内的引号，避免被字符串里的 {}/[] 干扰。
    """
    t = text.strip()
    if t.startswith("```"):
        t = _strip_fences(t)

    start = next((i for i, ch in enumerate(t) if ch in "{["), -1)
    if start < 0:
        return t  # 没有 JSON 起始符，原样返回交给上层报错

    open_ch = t[start]
    close_ch = "}" if open_ch == "{" else "]"
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(t)):
        ch = t[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == open_ch:
            depth += 1
        elif ch == close_ch:
            depth -= 1
            if depth == 0:
                return t[start:i + 1]
    return t[start:]  # 未闭合：返回到末尾，交给修复/报错


def _strip_fences(text: str) -> str:
    t = text.strip()
    # 去掉 markdown 围栏
    if t.startswith("```"):
        lines = t.split("\n")
        t = "\n".join(lines[1:])
        if t.rstrip().endswith("```"):
            t = t.rstrip()[:-3]
    # 去掉末尾反引号（可能的残留）
    t = t.rstrip().rstrip("`").strip()
    return t
