"""发布前应发现丢失引用和不完整的技能包。"""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate.py"
spec = importlib.util.spec_from_file_location("validate_skill", SCRIPT)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ValidationTests(unittest.TestCase):
    def test_missing_entry(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertTrue(validator.validate(directory))

    def test_broken_reference_is_found_then_resolved(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "SKILL.md").write_text(
                "---\nname: example-skill\ndescription: 一个测试用技能\n---\n"
                "[参考](references/review.md)\n",
                encoding="utf-8",
            )
            self.assertTrue(validator.validate(root))
            (root / "references").mkdir()
            (root / "references" / "review.md").write_text(
                "# 审阅\n", encoding="utf-8"
            )
            self.assertEqual(validator.validate(root), [])

    def test_reference_must_stay_in_package(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "package"
            root.mkdir()
            (Path(directory) / "outside.md").write_text("outside", encoding="utf-8")
            (root / "SKILL.md").write_text(
                "---\nname: example-skill\ndescription: 一个测试用技能\n---\n"
                "[外部](../outside.md)\n",
                encoding="utf-8",
            )
            self.assertTrue(validator.validate(root))


if __name__ == "__main__":
    unittest.main()
