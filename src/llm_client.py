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
         _reasoning_tokens: int = 4000) -> str:
    """统一对话入口。messages=[{"role":"user","content":...}]，返回文本。

    json=True 时不依赖 response_format（DeepSeek 推理模型不支持），
    而是往 messages 末尾追加一行要求，用 _strip_fences 去围栏后返回。
    _reasoning_tokens：分配给推理链的 token 预算（仅推理模型使用）。
    """
    import litellm  # 延迟导入，未装时给清晰报错

    cfg = get_config().get("llm", {})
    if system:
        messages = [{"role": "system", "content": system}, *messages]

    # json 通过 prompt 要求而非 response_format（兼容所有模型）
    if json:
        messages = [*messages, {"role": "user",
                     "content": "\n只输出 JSON，不要解释，不要 markdown 围栏。"}]

    last_err: Exception | None = None
    for cand in _candidates():
        try:
            params = _provider_params(cand["provider"], cand["model"])
        except LLMUnavailable as e:
            last_err = e
            continue

        # 推理模型需要给 reasoning_effort / extra_body
        model_name = params.get("model", "")
        is_deepseek = "deepseek" in model_name.lower()
        is_reasoning = is_deepseek or "-r1" in model_name.lower()

        # 推理模型多分配 token 给推理链（不设 reasoning_effort，避免 API 报错）
        kwargs = params | {
            "messages": messages,
            "temperature": cfg.get("temperature", 0.3),
            "max_tokens": (max_tokens or cfg.get("max_tokens", 4000)),
        }
        if is_reasoning:
            kwargs["max_tokens"] = kwargs["max_tokens"] + _reasoning_tokens

        try:
            resp = litellm.completion(**kwargs)
            msg = resp["choices"][0]["message"]
            content = msg.get("content") or ""
            if not content and is_reasoning:
                # 推理模型有时 content 为空，尝试 reasoning_content 或降级重试
                content = msg.get("reasoning_content") or ""
            return _strip_fences(content) if json else content
        except Exception as e:
            log.warning("LLM 调用失败（%s/%s）：%s，尝试降级",
                        cand["provider"], cand["model"], e)
            last_err = e
            continue

    raise RuntimeError(f"所有 LLM 候选均不可用：{last_err}")


def chat_json(messages: list[dict], *, system: str | None = None,
              max_tokens: int | None = None):
    """要求 JSON 输出并解析为 Python 对象。"""
    raw = chat(messages, system=system, max_tokens=max_tokens, json=True,
               _reasoning_tokens=4000)
    # 推理模型可能把 JSON 放在最后一段 reasoning_content 之后
    return _json.loads(raw)


def _strip_fences(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        t = t.split("\n", 1)[-1]
        if t.rstrip().endswith("```"):
            t = t.rstrip()[:-3]
    return t.strip()
