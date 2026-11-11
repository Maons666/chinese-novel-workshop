"""验证会影响交付判断的统计口径与只读行为。"""
import hashlib
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "text_stats.py"
spec = importlib.util.spec_from_file_location("text_stats", SCRIPT)
stats = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stats)


class TextStatsTests(unittest.TestCase):
    def test_mixed_text_and_original_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "章.md"
            raw = "\ufeff# 标题\r\n春风 A1，𠮷〇\n".encode("utf-8")
            path.write_bytes(raw)
            full = stats.measure(path)
            body = stats.measure(path, skip_headings=True)
            self.assertEqual(full["han_characters"], 6)
            self.assertEqual(body["han_characters"], 4)
            self.assertEqual(body["non_whitespace_characters"], 7)
            self.assertEqual(body["sha256"], hashlib.sha256(raw).hexdigest())
            self.assertEqual(path.read_bytes(), raw)

    def test_no_implicit_annotation_exclusion(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "draft.md"
            path.write_text("正文\n【批注】\n", encoding="utf-8")
            self.assertEqual(stats.measure(path)["han_characters"], 4)

    def test_bad_encoding_fails_without_touching_input(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.md"
            path.write_bytes(b"\xff\xfe\x00")
            before = path.read_bytes()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(path)], capture_output=True
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(path.read_bytes(), before)

    def test_missing_input_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(Path(directory) / "missing.md")],
                capture_output=True,
            )
            self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
