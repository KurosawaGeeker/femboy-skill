#!/usr/bin/env python3
"""Shared helpers for dependency-free community content validation."""

from __future__ import annotations

import json
import re
from pathlib import Path


def load_taxonomy(path: Path, *keys: str) -> tuple[set[str], ...]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return tuple(set(data[key]) for key in keys)


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
