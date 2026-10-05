# StableMatch deployment evidence

## Status

No canonical deployment or signing transaction has been performed. No deployer wallet, contract address, transaction hash, definition receipt, qualification receipt, matching hash, or chain source identity is claimed.

The extracted folder is connected only to `https://github.com/Ifem1/stablematch.git`. The live deployment must wait until the reviewed local checkpoint is pushed and the commit-pinned public fixture URLs are available.

## Local gates

- Unit/property suite: **12 passed**.
- Direct Mode suite: **32 passed** using the pinned stable GenVM `v0.2.16` artifact.
- GenVM lint: **3 checks passed**.
- GenVM SDK semantic validation: **passed**, contract `StableMatch`, 21 methods (9 views, 12 writes).
- Python compileall: **passed**.
- Repository preflight: **passed**, contract SHA-256 `51a9036af0533599c98aebfeb54bc0271a8c3dcecbb33198d3cead2a80d3f073`.
- Repository-local CLI: `genlayer@0.39.1`.
- Last observed network info: Studionet chain ID `61999`, RPC `https://studio.genlayer.com/api`.

Before every future signing or deployment stage, rerun `npm run genlayer -- network info` and independently verify chain ID `61999` and RPC `https://studio.genlayer.com/api`. Do not copy the last observed network response as evidence for a later signing stage.

## Required live fields

Populate this section only from verified chain responses and transaction receipts after completing [`LIVE_TEST_PLAN.md`](LIVE_TEST_PLAN.md): repository HEAD, contract Git blob, LF-normalized source SHA-256, deployed source identity, deployer, contract address, full deployment and lifecycle transaction hashes, definition hash, six qualification statuses and receipt hashes, final assignments, matching hash, zero blocking-pair count, and correct-/wrong-hash composition reads.

No live evidence is fabricated or inferred from local tests.
