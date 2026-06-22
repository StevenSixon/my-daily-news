"""LLM 调用超时透传（防止进程无限挂起）。"""
import litellm

from src import llm_client


def test_timeout_passed_to_litellm(monkeypatch):
    captured = {}

    def fake_completion(**kwargs):
        captured.update(kwargs)
        return {"choices": [{"message": {"content": "ok"}}]}

    monkeypatch.setattr(litellm, "completion", fake_completion)
    monkeypatch.setattr(llm_client, "_candidates",
                        lambda: [{"provider": "openai", "model": "gpt-x"}])
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")

    out = llm_client.chat([{"role": "user", "content": "hi"}])
    assert out == "ok"
    # config 默认 timeout_seconds = 1800（30 分钟）
    assert captured.get("timeout") == 1800
