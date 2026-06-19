"""本地存储：项目库目录 + 全局索引 data/index.json。"""
from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

from .config_loader import ROOT, get_config
from .utils import repo_slug


def _atomic_write_text(path: Path, text: str) -> None:
    """写临时文件 + os.replace 原子替换，避免写入中断损坏目标文件。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp, path)  # 同一文件系统内原子替换
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise

INDEX_PATH = ROOT / "data" / "index.json"
CLASSIFY_LOG = ROOT / "data" / "classify-log.jsonl"


def projects_root() -> Path:
    d = ROOT / get_config().get("report", {}).get("projects_dir", "projects")
    d.mkdir(parents=True, exist_ok=True)
    return d


def daily_root() -> Path:
    d = ROOT / get_config().get("report", {}).get("daily_dir", "daily")
    d.mkdir(parents=True, exist_ok=True)
    return d


def project_dir(full_name: str) -> Path:
    d = projects_root() / repo_slug(full_name)
    d.mkdir(parents=True, exist_ok=True)
    return d


def project_dir_relative(full_name: str) -> str:
    """日报里用的相对路径：../projects/owner__repo"""
    projects_dir = get_config().get("report", {}).get("projects_dir", "projects")
    return f"../{projects_dir}/{repo_slug(full_name)}"


def load_index() -> dict:
    if INDEX_PATH.exists():
        with open(INDEX_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_index(index: dict) -> None:
    _atomic_write_text(INDEX_PATH, json.dumps(index, ensure_ascii=False, indent=2))


def read_json(path: Path) -> dict | None:
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return None


def write_json(path: Path, data) -> None:
    _atomic_write_text(path, json.dumps(data, ensure_ascii=False, indent=2))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def append_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(text)


def append_jsonl(path: Path, obj) -> None:
    """追加一行 JSON（审计日志用）。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")
