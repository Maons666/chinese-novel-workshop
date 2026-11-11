#!/usr/bin/env python3
"""只读统计 UTF-8 文本；不判断文笔、不自动补写或截断。"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata


def is_han(char):
    """使用当前 Python Unicode 数据库：统一/兼容汉字及〇。"""
    name = unicodedata.name(char, "")
    return char == "〇" or name.startswith(
        ("CJK UNIFIED IDEOGRAPH-", "CJK COMPATIBILITY IDEOGRAPH-")
    )


def measure(path, skip_headings=False):
    raw = Path(path).read_bytes()
    text = raw.decode("utf-8-sig")
    if skip_headings:
        # 仅排除 ATX 标题行；不声称识别全部 Markdown 或作者批注。
        text = "".join(
            line for line in text.splitlines(keepends=True)
            if not re.match(r"^ {0,3}#{1,6}(?:\s|$)", line)
        )
    return {
        "path": str(Path(path)),
        "scope": "排除 ATX 标题行" if skip_headings else "全文件",
        "han_characters": sum(is_han(char) for char in text),
        "non_whitespace_characters": sum(not char.isspace() for char in text),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "unicode_version": unicodedata.unidata_version,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument(
        "--skip-headings", action="store_true",
        help="排除形如 # 标题 的行；批注、占位、代码等仍计入",
    )
    args = parser.parse_args(argv)
    results, errors = [], []
    for path in args.paths:
        try:
            results.append(measure(path, args.skip_headings))
        except (OSError, UnicodeError) as exc:
            errors.append({"path": str(path), "error": str(exc)})
    print(json.dumps(results, ensure_ascii=False, indent=2))
    if errors:
        print(json.dumps(errors, ensure_ascii=False, indent=2), file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
