"""学习：拉 README/docs/release → LLM 生成报告 → 写入项目库（持续迭代）。"""
from __future__ import annotations

from . import llm_client
from .config_loader import env, get_config
from .github_client import GitHubClient
from .store import (project_dir, project_dir_relative, read_json, write_json,
                    write_text, append_text)
from .utils import get_logger, now_iso, today_str

log = get_logger()

_ANALYSIS_SYS = (
    "你是资深技术分析师，面向想快速判断项目是否值得深入的极客读者。"
    "语言简洁、说人话、不要营销腔；README 没写清的不要编，标注信息不足。"
)


def _client() -> GitHubClient:
    return GitHubClient(token=env("GITHUB_TOKEN"))


def _should_revisit(item: dict, meta: dict | None, release: dict | None) -> tuple[bool, str]:
    """老项目是否需要重新调 LLM 重学。"""
    cfg = get_config()["analyze_revisit"]
    if meta is None:
        return True, "new"
    if cfg.get("on_new_release") and release:
        if release.get("tag") and release["tag"] != meta.get("latest_release"):
            return True, "release_update"
    last = meta.get("stars_total", 0)
    if last and item["stars_total"] >= last * (1 + cfg["on_star_jump_pct"] / 100):
        return True, "star_jump"
    return False, "no_change"


def _build_context(gh: GitHubClient, full_name: str, detail: dict,
                   release: dict | None) -> tuple[str, str]:
    """组装喂给 LLM 的上下文，返回 (context, readme_text)。"""
    max_chars = get_config()["analyze"]["max_readme_chars"]
    readme = gh.readme(full_name)
    readme_trunc = readme[:max_chars]

    docs = gh.list_dir(full_name, "docs")
    examples = gh.list_dir(full_name, "examples")

    parts = [
        f"# 仓库：{full_name}",
        f"描述：{detail.get('description','')}",
        f"语言：{detail.get('language')} | 主题：{detail.get('topics')} | 许可：{detail.get('license')}",
        f"Star：{detail.get('stars_total')} | 创建：{detail.get('created_at')} | 最近推送：{detail.get('pushed_at')}",
        f"主页：{detail.get('homepage')}",
    ]
    if release:
        parts.append(f"最新 Release：{release.get('tag')} ({release.get('published_at')})\n"
                     f"Release 说明（截断）：\n{release.get('body','')}")
    if docs:
        parts.append(f"docs/ 目录：{docs[:30]}")
    if examples:
        parts.append(f"examples/ 目录：{examples[:30]}")
    parts.append(f"\n# README（截断到 {max_chars} 字）：\n{readme_trunc}")
    return "\n".join(parts), readme


def _gen_report(context: str) -> dict:
    """调用 LLM 生成结构化报告。"""
    prompt = (
        context
        + "\n\n请基于以上信息输出 JSON：\n"
        "{\n"
        '  "one_liner": "一句话亮点（30字内）",\n'
        '  "analysis_md": "Markdown 深度报告，含小标题：## 它是什么 / ## 为什么火 / '
        '## 技术栈 / ## 核心能力 / ## 适用场景 / ## 同类对比 / ## 版本动态",\n'
        '  "quickstart_md": "Markdown 上手指南：安装、最小可用示例、依赖前提"\n'
        "}\n只输出 JSON。"
    )
    return llm_client.chat_json([{"role": "user", "content": prompt}], system=_ANALYSIS_SYS)


def learn(item: dict, index: dict) -> dict:
    """对单个项目执行学习并写入项目库；返回供日报用的摘要条目。同时就地更新 index。"""
    full_name = item["full_name"]
    pdir = project_dir(full_name)
    meta_path = pdir / "metadata.json"
    meta = read_json(meta_path)

    gh = _client()
    detail = gh.repo(full_name) or item
    release = gh.latest_release(full_name)

    revisit, reason = _should_revisit(detail, meta, release)
    is_new = meta is None
    today = today_str()

    if revisit and llm_client.available():
        context, readme = _build_context(gh, full_name, detail, release)
        try:
            report = _gen_report(context)
            write_text(pdir / "analysis.md", report.get("analysis_md", ""))
            write_text(pdir / "quickstart.md", report.get("quickstart_md", ""))
            write_text(pdir / "README.snapshot.md", readme)
            one_liner = report.get("one_liner", detail.get("description", ""))
            log.info("已学习 %s（%s）", full_name, reason)
        except Exception as e:
            log.warning("学习 %s 失败：%s", full_name, e)
            one_liner = (meta or {}).get("one_liner") or detail.get("description", "")
            revisit = False
    else:
        if revisit and not llm_client.available():
            log.info("跳过 LLM（无可用 key），仅更新 %s 元数据", full_name)
        one_liner = (meta or {}).get("one_liner") or detail.get("description", "")
        reason = "lightweight"
        revisit = False  # 未实际生成报告，勿更新 analysis_updated_at

    # 更新 metadata（持续迭代）
    appearances = (meta or {}).get("appearances", [])
    appearances.append({
        "date": today,
        "reason": "new" if is_new else reason,
        "stars_total": detail.get("stars_total"),
        "stars_gained": item.get("stars_gained", 0),
        "release": release.get("tag") if release else None,
    })
    streak = 1 if is_new else (meta.get("streak_days", 1) + 1)
    new_meta = {
        "full_name": full_name,
        "url": detail.get("url"),
        "description": detail.get("description", ""),
        "language": detail.get("language"),
        "topics": detail.get("topics", []),
        "license": detail.get("license"),
        "category": item.get("category", "AI 应用"),
        "classify_reason": item.get("classify_reason", (meta or {}).get("classify_reason", "")),
        "one_liner": one_liner,
        "stars_total": detail.get("stars_total"),
        "created_at": detail.get("created_at"),
        "pushed_at": detail.get("pushed_at"),
        "latest_release": release.get("tag") if release else (meta or {}).get("latest_release"),
        "first_seen": (meta or {}).get("first_seen", today),
        "last_seen": today,
        "streak_days": streak,
        "analysis_updated_at": now_iso() if revisit else (meta or {}).get("analysis_updated_at"),
        "appearances": appearances,
    }
    write_json(meta_path, new_meta)

    # history.md 只追加
    append_text(
        pdir / "history.md",
        f"- {today} | {'🆕新发现' if is_new else reason} | "
        f"⭐{detail.get('stars_total')}(+{item.get('stars_gained',0)}) | "
        f"release={release.get('tag') if release else '-'}\n",
    )

    # 更新全局索引
    index[full_name] = {
        "dir": f"{get_config()['report']['projects_dir']}/{full_name.replace('/', '__')}",
        "first_seen": new_meta["first_seen"],
        "last_seen": today,
        "streak_days": streak,
        "last_release_seen": new_meta["latest_release"],
        "last_stars_total": detail.get("stars_total"),
    }

    return {
        "full_name": full_name,
        "url": detail.get("url"),
        "one_liner": one_liner,
        "language": detail.get("language"),
        "stars_total": detail.get("stars_total"),
        "stars_gained": item.get("stars_gained", 0),
        "streak_days": streak,
        "is_new": is_new,
        "refreshed": bool(revisit),  # 本轮是否实际重生成了报告（供日报筛选）
        "revisit_reason": reason,
        "report_path": f"{project_dir_relative(full_name)}/analysis.md",
    }
