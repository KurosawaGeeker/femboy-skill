#!/usr/bin/env python3
"""Validate community consumer records, category placement, links, and index entries."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from community_validation import load_taxonomy, parse_frontmatter


ROOT = Path(__file__).resolve().parents[1]
CONSUMER = ROOT / "femboy-skill" / "consumer"
CONTROL_FILES = {"README.md", "INDEX.md", "_template.md"}
REQUIRED = {
    "name",
    "type",
    "category",
    "link",
    "adult_only",
    "experienced_by_contributor",
    "commercial_relationship",
}
FILENAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
REQUIRED_HEADINGS = {
    "## 怎么消费或使用（必填）",
    "## 推荐理由（必填）",
    "## 缺点与不适合谁（必填）",
}


def validate_record(
    path: Path,
    index: str,
    types: set[str],
    categories: set[str],
    relationships: set[str],
) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(CONSUMER)
    content = path.read_text(encoding="utf-8")

    if not FILENAME.fullmatch(path.name):
        errors.append(f"{relative}: 文件名应为 lowercase-name.md")

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

    if metadata.get("type") not in types:
        errors.append(f"{relative}: type 不在允许列表中")

    category = metadata.get("category")
    if category not in categories:
        errors.append(f"{relative}: category 不在允许列表中")
    elif path.parent.name != category:
        errors.append(f"{relative}: category 应与所在目录 {path.parent.name} 一致")

    link = metadata.get("link", "")
    parsed_link = urlparse(link)
    if parsed_link.scheme != "https" or not parsed_link.netloc:
        errors.append(f"{relative}: link 必须是完整 HTTPS 链接")

    if metadata.get("adult_only") not in {"true", "false"}:
        errors.append(f"{relative}: adult_only 必须为 true 或 false")
    if metadata.get("experienced_by_contributor") != "true":
        errors.append(f"{relative}: experienced_by_contributor 必须为 true")
    if metadata.get("commercial_relationship") not in relationships:
        errors.append(f"{relative}: commercial_relationship 不在允许列表中")

    for heading in sorted(REQUIRED_HEADINGS):
        if heading not in content:
            errors.append(f"{relative}: 缺少正文段落 {heading}")
    if relative.as_posix() not in index:
        errors.append(f"{relative}: 尚未加入 INDEX.md")

    return errors


def main() -> int:
    types, categories, relationships = load_taxonomy(
        CONSUMER / "taxonomy.json",
        "types",
        "categories",
        "commercial_relationships",
    )
    index = (CONSUMER / "INDEX.md").read_text(encoding="utf-8")
    records = sorted(
        path
        for path in CONSUMER.rglob("*.md")
        if path.name not in CONTROL_FILES
    )
    errors = [
        error
        for path in records
        for error in validate_record(path, index, types, categories, relationships)
    ]

    for category in sorted(categories):
        if not (CONSUMER / category / "README.md").is_file():
            errors.append(f"taxonomy.json: 类目 {category} 缺少目录 README.md")

    if records and "当前尚无已合并消费记录" in index:
        errors.append("INDEX.md: 已有记录时请删除“当前尚无已合并消费记录”")

    if errors:
        print("消费指南校验失败：", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"消费指南校验通过：{len(records)} 条记录。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
