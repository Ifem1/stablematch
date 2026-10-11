from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIRS = {
    ".git",
    ".venv",
    ".npm-cache",
    ".tooling",
    ".pytest_cache",
    "__pycache__",
    "node_modules",
    "artifacts",
}

entries: list[tuple[str, str]] = []
for directory, child_dirs, filenames in os.walk(ROOT):
    child_dirs[:] = [name for name in child_dirs if name not in GENERATED_DIRS]
    for filename in filenames:
        path = Path(directory) / filename
        relative = path.relative_to(ROOT).as_posix()
        if relative != "MANIFEST.sha256":
            entries.append((relative, hashlib.sha256(path.read_bytes()).hexdigest()))

manifest = "".join(f"{digest}  {relative}\n" for relative, digest in sorted(entries))
(ROOT / "MANIFEST.sha256").write_text(manifest, encoding="utf-8", newline="\n")
