"""配置与环境加载：config.yaml + .env。"""
from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent

# 加载 .env（密钥）。已存在的真实环境变量优先。
load_dotenv(ROOT / ".env")


@lru_cache(maxsize=1)
def get_config() -> dict:
    """读取 config/config.yaml 为 dict（缓存）。"""
    with open(ROOT / "config" / "config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def env(key: str, default: str | None = None) -> str | None:
    """读取环境变量；空字符串视为未设置。"""
    val = os.getenv(key, default)
    if val is not None and val.strip() == "":
        return default
    return val


def require_env(key: str) -> str:
    val = env(key)
    if not val:
        raise RuntimeError(f"缺少必要的环境变量 {key}，请在 .env 中配置。")
    return val
