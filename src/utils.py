"""通用工具：时间、slug、日志。"""
from __future__ import annotations

import logging
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from .config_loader import ROOT, get_config

_LOGGER_READY = False


def tz() -> ZoneInfo:
    return ZoneInfo(get_config().get("report", {}).get("timezone", "Asia/Shanghai"))


def now() -> datetime:
    return datetime.now(tz())


def today_str() -> str:
    return now().strftime("%Y-%m-%d")


def now_iso() -> str:
    return now().strftime("%Y-%m-%dT%H:%M:%S%z")


def repo_slug(full_name: str) -> str:
    """owner/repo -> owner__repo（可安全作为目录名）。"""
    return full_name.replace("/", "__")


def parse_int(text: str) -> int:
    """从 '1,234 stars today' 之类文本里抽出整数。"""
    digits = re.sub(r"[^\d]", "", text or "")
    return int(digits) if digits else 0


def get_logger(name: str = "daily-news") -> logging.Logger:
    """控制台 + 当天日志文件。"""
    global _LOGGER_READY
    logger = logging.getLogger(name)
    if _LOGGER_READY:
        return logger

    logger.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%H:%M:%S")

    console = logging.StreamHandler()
    console.setFormatter(fmt)
    logger.addHandler(console)

    logs_dir = ROOT / "logs"
    logs_dir.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(logs_dir / f"{today_str()}.log", encoding="utf-8")
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)

    _LOGGER_READY = True
    return logger
