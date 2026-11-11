#!/usr/bin/env python3
"""检查技能包的 UTF-8、入口元数据与相对文档链接；不评判写作质量。"""
import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def validate(root):
    root = Path(root).resolve()
    errors = []
    entry = root / "SKILL.md"
    if not entry.is_file():
        return ["缺少 SKILL.md"]
    documents = {}
    for path in sorted(root.rglob("*")):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        if path.is_file() and path.suffix in {".md", ".py", ".yaml", ".yml"}:
            try:
                data = path.read_bytes()
                if data.startswith(b"\xef\xbb\xbf"):
                    errors.append(f"{path.relative_to(root)}: 请保存为无 BOM UTF-8")
                documents[path] = data.decode("utf-8")
            except (OSError, UnicodeError) as exc:
                errors.append(f"{path.relative_to(root)}: 无法读取 UTF-8: {exc}")
    text = documents.get(entry, "")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        errors.append("SKILL.md: 缺少 YAML frontmatter")
    else:
        header = match.group(1)
        names = re.findall(r"^name:\s*([a-z0-9-]+)\s*$", header, re.M)
        if len(names) != 1 or len(names[0]) >= 64:
            errors.append("SKILL.md: name 应是少于 64 字符的小写连字符名称")
        if not re.search(r"^description:\s*\S.+$", header, re.M):
            errors.append("SKILL.md: 缺少非空单行 description")
    if len(text.splitlines()) > 200:
        errors.append("SKILL.md: 入口过长，请将专项细节下沉到 references")
    for path, content in documents.items():
        if path.suffix != ".md":
            continue
        for target in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^\s)]+)\)", content):
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            local = unquote(target.split("#", 1)[0])
            if not local:
                continue
            resolved = (path.parent / local).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                errors.append(f"{path.relative_to(root)}: 链接越出仓库: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(root)}: 链接不存在: {target}")
    # 发布物不应依赖维护者某台机器的绝对路径。
    for path, content in documents.items():
        if path.suffix == ".md" and re.search(r"[A-Z]:[\\/](?:Users|Personal)[\\/]", content):
            errors.append(f"{path.relative_to(root)}: 包含本机绝对路径")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    errors = validate(args.root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("通过：UTF-8、入口元数据、相对链接和可移植路径检查。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
