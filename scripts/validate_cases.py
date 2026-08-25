#!/usr/bin/env python3
"""Validate community case filenames, classification metadata, and index entries."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "femboy-guide" / "references" / "cases"
CONTROL_FILES = {"README.md", "INDEX.md", "_template.md"}
REQUIRED = {"title", "category", "experience_level", "outcome", "adult", "anonymized"}
FILENAME = re.compile(r"^\d{4}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")


def load_taxonomy() -> tuple[set[str], set[str], set[str]]:
    data = json.loads((CASES / "taxonomy.json").read_text(encoding="utf-8"))
    return (
        set(data["categories"]),
        set(data["experience_levels"]),
        set(data["outcomes"]),
    )


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("缺少 YAML frontmatter 起始标记")

    metadata: dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            return metadata
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([a-z_]+):\s*(.*?)\s*$", line)
        if match:
            metadata[match.group(1)] = match.group(2).strip('"\'')
    raise ValueError("缺少 YAML frontmatter 结束标记")


def validate_case(
    path: Path,
    index: str,
    categories: set[str],
    experience_levels: set[str],
    outcomes: set[str],
) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(CASES)

    if not FILENAME.fullmatch(path.name):
        errors.append(f"{relative}: 文件名应为 YYYY-MM-english-slug.md")

    try:
        metadata = parse_frontmatter(path)
    except ValueError as exc:
        return [f"{relative}: {exc}"]

    missing = sorted(REQUIRED - metadata.keys())
    if missing:
        errors.append(f"{relative}: 缺少必填字段 {', '.join(missing)}")
    empty = sorted(key for key in REQUIRED if key in metadata and not metadata[key])
    if empty:
        errors.append(f"{relative}: 必填字段不能为空 {', '.join(empty)}")

    category = metadata.get("category")
    if category not in categories:
        errors.append(f"{relative}: category 不在允许列表中")
    elif path.parent.name != category:
        errors.append(f"{relative}: category 应与所在目录 {path.parent.name} 一致")

    if metadata.get("experience_level") not in experience_levels:
        errors.append(f"{relative}: experience_level 不在允许列表中")
    if metadata.get("outcome") not in outcomes:
        errors.append(f"{relative}: outcome 不在允许列表中")
    if metadata.get("adult") != "true":
        errors.append(f"{relative}: adult 必须为 true")
    if metadata.get("anonymized") != "true":
        errors.append(f"{relative}: anonymized 必须为 true")
    if relative.as_posix() not in index:
        errors.append(f"{relative}: 尚未加入 INDEX.md")

    return errors


def main() -> int:
    categories, experience_levels, outcomes = load_taxonomy()
    index_path = CASES / "INDEX.md"
    index = index_path.read_text(encoding="utf-8")
    cases = sorted(
        path
        for path in CASES.rglob("*.md")
        if path.name not in CONTROL_FILES
    )
    errors = [
        error
        for path in cases
        for error in validate_case(
            path,
            index,
            categories,
            experience_levels,
            outcomes,
        )
    ]

    for category in sorted(categories):
        if not (CASES / category / "README.md").is_file():
            errors.append(f"taxonomy.json: 类目 {category} 缺少目录 README.md")

    if cases and "当前尚无已合并案例" in index:
        errors.append("INDEX.md: 已有案例时请删除“当前尚无已合并案例”")

    if errors:
        print("案例校验失败：", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"案例校验通过：{len(cases)} 个案例。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
