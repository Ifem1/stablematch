from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import sys

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
REQUIRED = [
    "README.md",
    "SUBMISSION.md",
    "BUILD_STATUS.md",
    "NETWORK_LOCK.json",
    "contracts/stablematch.py",
    "reference/stablematch_model.py",
    "tests/unit/test_stablematch_model.py",
    "tests/direct/test_stablematch.py",
    "docs/ARCHITECTURE.md",
    "docs/SECURITY_MODEL.md",
    "docs/LIVE_TEST_PLAN.md",
    "docs/DEPLOYMENT.md",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)

for rel in REQUIRED:
    if not (ROOT / rel).exists():
        fail(f"missing {rel}")

manifest_path = ROOT / "MANIFEST.sha256"
if not manifest_path.exists():
    fail("MANIFEST.sha256 is missing")
manifest_paths = set()
for line_no, line in enumerate(manifest_path.read_text(encoding="utf-8").splitlines(), start=1):
    parts = line.split("  ", 1)
    if len(parts) != 2 or not re.fullmatch(r"[0-9a-f]{64}", parts[0]):
        fail(f"malformed MANIFEST.sha256 line {line_no}")
    rel = parts[1].removeprefix("./").replace("/", "/")
    target = (ROOT / rel).resolve()
    if ROOT not in target.parents or not target.is_file():
        fail(f"manifest path is missing or escapes the repository: {rel}")
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    if digest != parts[0]:
        fail(f"manifest checksum mismatch: {rel}")
    manifest_paths.add(rel.replace("\\", "/"))

actual_paths = set()
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [name for name in dirnames if name not in GENERATED_DIRS]
    for filename in filenames:
        path = Path(dirpath) / filename
        rel = path.relative_to(ROOT).as_posix()
        if rel != "MANIFEST.sha256":
            actual_paths.add(rel)
if actual_paths != manifest_paths:
    missing = sorted(actual_paths - manifest_paths)
    stale = sorted(manifest_paths - actual_paths)
    fail(f"manifest coverage mismatch: missing={missing[:3]} stale={stale[:3]}")

lock = json.loads((ROOT / "NETWORK_LOCK.json").read_text(encoding="utf-8"))
if lock["chain_id"] != 61999 or lock["rpc"] != "https://studio.genlayer.com/api":
    fail("NETWORK_LOCK does not pin Studionet 61999")
if lock["cli"] != "genlayer@0.39.1":
    fail("CLI is not pinned to genlayer@0.39.1")
if lock.get("direct_mode_genvm") != "v0.2.16":
    fail("Direct Mode must pin the stable GenVM v0.2.16 artifact")
if lock.get("genvm_linter") != "genvm-linter==0.11.0":
    fail("GenVM linter version is not pinned")

package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
if package.get("devDependencies", {}).get("genlayer") != "0.39.1":
    fail("repository-local GenLayer CLI must be exactly 0.39.1")
if package.get("scripts", {}).get("genlayer") != "npx --no-install genlayer":
    fail("GenLayer CLI script must use the repository-local installation")
config = (ROOT / "gltest.config.yaml").read_text(encoding="utf-8")
if "default: localnet" not in config or "url: https://studio.genlayer.com/api" not in config:
    fail("test config must default to localnet and pin canonical Studionet RPC")
direct_config = (ROOT / "tests/direct/conftest.py").read_text(encoding="utf-8")
if 'sdk_version="v0.2.16"' not in direct_config:
    fail("Direct Mode test deployment must explicitly use stable GenVM v0.2.16")
sdk_setup = (ROOT / "scripts/prepare_stable_sdk.ps1").read_text(encoding="utf-8")
if "$stableGenVm = 'v0.2.16'" not in sdk_setup:
    fail("SDK setup script must remain pinned to stable GenVM v0.2.16")

all_text = "\n".join(
    p.read_text(encoding="utf-8", errors="ignore")
    for p in ROOT.rglob("*")
    if p.is_file()
    and not any(part in GENERATED_DIRS for part in p.relative_to(ROOT).parts)
    and p != Path(__file__).resolve()
    and p.suffix.lower() in {".py", ".md", ".txt", ".json", ".yaml", ".yml"}
)

# 61997 may appear only inside NETWORK_LOCK as an explicit forbidden value and in
# documentation that warns against it. Deployment commands/RPCs are forbidden.
for forbidden in ("https://studio-dev.genlayer.com/api", "https://studio-next.genlayer.com/api"):
    if forbidden in all_text:
        fail(f"forbidden Studio-dev RPC appears in repository: {forbidden}")

contract = (ROOT / "contracts/stablematch.py").read_text(encoding="utf-8")
if 'py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6' not in contract:
    fail("stable py-genlayer dependency header missing")
if "run_nondet_unsafe" not in contract:
    fail("custom validator consensus path missing")
if "blocking_pair_count" not in contract:
    fail("stability invariant view missing")
if re.search(r"frontend|next\.js|react", contract, re.I):
    fail("frontend concern leaked into contract")

lockfile = ROOT / "package-lock.json"
if lockfile.exists():
    npm_lock = json.loads(lockfile.read_text(encoding="utf-8"))
    locked = npm_lock.get("packages", {}).get("node_modules/genlayer", {}).get("version")
    if locked != "0.39.1":
        fail("package-lock.json does not lock genlayer@0.39.1")
    serialized = lockfile.read_text(encoding="utf-8").lower()
    if "studio-dev.genlayer.com" in serialized or "studio-next.genlayer.com" in serialized:
        fail("forbidden RPC appears in package-lock.json")

sha = hashlib.sha256(contract.replace("\r\n", "\n").encode()).hexdigest()
print("PASS: StableMatch preflight")
print(f"contract_sha256={sha}")
print("network=studionet chain_id=61999 rpc=https://studio.genlayer.com/api")
