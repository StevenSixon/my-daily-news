"""原子写入（I-6 回归）+ jsonl 追加。"""
import json

from src import store


def test_write_json_roundtrip_unicode(tmp_path):
    p = tmp_path / "sub" / "index.json"
    store.write_json(p, {"a": 1, "中文": True})
    assert json.loads(p.read_text(encoding="utf-8")) == {"a": 1, "中文": True}


def test_write_json_no_tmp_leftover(tmp_path):
    p = tmp_path / "index.json"
    store.write_json(p, {"x": 1})
    leftovers = [f.name for f in tmp_path.iterdir() if f.suffix == ".tmp"]
    assert leftovers == []


def test_write_json_overwrites_atomically(tmp_path):
    p = tmp_path / "index.json"
    store.write_json(p, {"v": 1})
    store.write_json(p, {"v": 2})
    assert json.loads(p.read_text(encoding="utf-8")) == {"v": 2}


def test_append_jsonl(tmp_path):
    p = tmp_path / "log.jsonl"
    store.append_jsonl(p, {"i": 1})
    store.append_jsonl(p, {"i": 2, "中文": "x"})
    lines = p.read_text(encoding="utf-8").strip().splitlines()
    assert [json.loads(x) for x in lines] == [{"i": 1}, {"i": 2, "中文": "x"}]
