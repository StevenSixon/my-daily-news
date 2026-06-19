"""飞书自建应用：tenant_access_token（带缓存）+ 发送交互卡片（P2P 私聊）。"""
from __future__ import annotations

import json
import os
import time

import requests

from .config_loader import ROOT, require_env
from .store import read_json, write_json
from .utils import get_logger

log = get_logger()

BASE = "https://open.feishu.cn/open-apis"
TOKEN_CACHE = ROOT / "data" / ".feishu_token.json"


def _tenant_access_token() -> str:
    """获取并缓存 tenant_access_token（有效期约 2h，提前 5 分钟刷新）。"""
    cached = read_json(TOKEN_CACHE)
    if cached and cached.get("expire_at", 0) - 300 > time.time():
        return cached["token"]

    app_id = require_env("FEISHU_APP_ID")
    app_secret = require_env("FEISHU_APP_SECRET")
    resp = requests.post(
        f"{BASE}/auth/v3/tenant_access_token/internal",
        json={"app_id": app_id, "app_secret": app_secret},
        timeout=20,
    )
    resp.raise_for_status()
    data = resp.json()
    if data.get("code") != 0:
        raise RuntimeError(f"获取 tenant_access_token 失败：{data}")

    token = data["tenant_access_token"]
    write_json(TOKEN_CACHE, {"token": token, "expire_at": time.time() + data.get("expire", 7200)})
    try:
        os.chmod(TOKEN_CACHE, 0o600)  # 凭证文件收紧为仅本人可读写
    except OSError as e:
        log.warning("收紧 token 缓存权限失败：%s", e)
    return token


def send_alert(title: str, lines: list[str], color: str = "red") -> None:
    """发送一条简短告警卡片（采集失败/无数据等异常路径用）。"""
    card = {
        "config": {"wide_screen_mode": True},
        "header": {"template": color,
                   "title": {"tag": "plain_text", "content": title}},
        "elements": [{"tag": "div", "text": {"tag": "lark_md", "content": "\n".join(lines)}}],
    }
    send_card(card)


def send_card(card: dict) -> None:
    """把交互卡片私聊推送给 .env 配置的接收者。"""
    receive_id = require_env("FEISHU_RECEIVE_ID")
    receive_id_type = require_env("FEISHU_RECEIVE_ID_TYPE")  # open_id | email | mobile | user_id
    token = _tenant_access_token()

    resp = requests.post(
        f"{BASE}/im/v1/messages",
        params={"receive_id_type": receive_id_type},
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json; charset=utf-8"},
        json={"receive_id": receive_id, "msg_type": "interactive",
              "content": json.dumps(card, ensure_ascii=False)},
        timeout=20,
    )
    data = resp.json()
    if data.get("code") != 0:
        raise RuntimeError(f"飞书发送失败：{data}")
    log.info("飞书推送成功，message_id=%s", data.get("data", {}).get("message_id"))
