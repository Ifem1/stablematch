# StableMatch build status

## Current verification (2026-10-05)

- Python 3.12.10, Node 24.16.0, npm 11.13.0.
- Exact extracted folder is a Git repository on `main`; `origin` is `https://github.com/Ifem1/stablematch.git` and was verified with `git remote -v`.
- Repository-local CLI resolves to `genlayer@0.39.1`.
- Official non-prerelease Direct Mode SDK is pinned to GenVM `v0.2.16`, which contains the contract's declared `py-genlayer` dependency hash. No v0.40 CLI or v0.6 preview SDK is used.
- Python tooling is installed in `.venv` from `requirements.txt` and `requirements-test.txt`.
- `python -m pytest tests/unit -v`: **12 passed**.
- `python -m pytest tests/direct -v`: **32 passed**.
- `python -m compileall contracts reference tests scripts examples`: passed.
- `python scripts/preflight.py`: passed; LF-normalized contract SHA-256 is `51a9036af0533599c98aebfeb54bc0271a8c3dcecbb33198d3cead2a80d3f073`.
- `genvm-lint check --json contracts/stablematch.py` with `GENVMROOT` set to the workspace-local stable SDK: 3 lint checks passed; semantic validation passed for 21 methods (9 views, 12 writes).
- Generated comparison coverage: 250 markets exercise the contract's actual deterministic helper against `reference/stablematch_model.py`; 500 additional unit markets compare the reference to an independent proposal-loop transcription.
- Full deterministic and Direct Mode gates are green. No signing or deployment has occurred.

## Changes made during finalization

- Evidence excerpts are checked byte-for-byte against one fetched page, so normalization and cross-page concatenation cannot manufacture a grounded excerpt.
- Source URL validation rejects private/local host suffixes, URL credentials, and numeric or alternate IP-literal encodings.
- Definition commitments include market, candidate, and opportunity owners, as well as the frozen preferences, requirements, capacities, evidence URLs, labels, and profiles.
- Matching mechanics are in a pure deterministic helper called by the contract. GenLayer only determines the eligibility graph.
- Direct Mode setup pins stable GenVM and contains a Windows-only test harness adapter for temporary stdin cleanup and clock refresh.
- Preflight enforces the network, CLI, Direct Mode SDK, and linter pins.

## Remaining before a complete submission

- Run the exact `npm run genlayer -- network info` verification immediately before any future signing/deployment. It currently reports Studionet 61999 and the canonical RPC, but this check must be repeated before each live stage.
- Push the reviewed checkpoint to `Ifem1/stablematch` after final diff review. No other remote is configured.
- Run the complete live lifecycle in `docs/LIVE_TEST_PLAN.md`, using commit-pinned raw fixture URLs, then fill `docs/DEPLOYMENT.md` with observed evidence only.
- Perform the final hostile review again against the deployed source identity and live composition readbacks.

No live transaction evidence, wallet, deployer, contract address, source identity, or lifecycle receipt is claimed in this file.
