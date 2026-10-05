# StableMatch

**Consensus establishes eligibility. Deterministic matching decides the assignment.**

StableMatch is a standalone GenLayer Intelligent Contract primitive for two-sided markets whose eligibility criteria are written in natural language but whose allocation should remain deterministic and mathematically stable.

A candidate and an opportunity each freeze their own preference order. GenLayer validators independently determine only whether the candidate's sealed public evidence establishes the opportunity's frozen mandatory requirements. Once every mutually listed pair is resolved, ordinary many-to-one Gale-Shapley matching produces the final assignment.

The LLM never chooses the winner.

## Core invariant

A finalized StableMatch market has **zero eligible mutually acceptable blocking pairs** under its exact frozen preferences and capacities.

That is stronger and more reusable than "AI ranks candidates".

## Why GenLayer

A normal smart contract can run Gale-Shapley perfectly well, but it cannot safely determine whether public evidence demonstrates a natural-language requirement such as "production security-review experience". A centralized oracle could provide that edge, but then one server controls who may participate.

StableMatch puts only that semantic boundary under GenLayer consensus. Everything after eligibility is deterministic.

## Protocol

```text
candidate evidence + opportunity requirements
                    |
                    v
        independent GenLayer consensus
                    |
             ELIGIBLE edges
                    |
                    v
        deterministic Gale-Shapley
                    |
                    v
     stable matching + matching hash
```

### Frozen market inputs

Candidates freeze public evidence URLs and ordered opportunity preferences.

Opportunities freeze mandatory requirements, capacity and ordered candidate preferences.

Market sealing commits the complete two-sided definition to `definition_hash`.

### Qualification

Only pairs listed by both sides may be qualified. Terminal outcomes are:

- `ELIGIBLE`
- `NOT_ESTABLISHED`

`AMBIGUOUS` and `UNAVAILABLE` fail closed and must be retried before the qualification deadline. Every mutually listed pair must be terminal before matching.

### Matching

Candidates propose in deterministic registration order. Each opportunity holds up to its frozen capacity according to its explicit preference order. Displaced candidates continue down their own preferences until the queue is exhausted.

The contract then recomputes the blocking-pair invariant. A non-zero count causes finalization to revert.

## Network

Canonical submission target:

- **Studionet**
- chain ID **61999**
- RPC `https://studio.genlayer.com/api`
- explorer `https://explorer-studio.genlayer.com`
- repository-local CLI `genlayer@0.39.1`

This repository is intentionally **not** a Studio-dev / 61997 build.

## No frontend

StableMatch is deliberately contract-only. There is no Next.js application, backend authority, hosted database, wallet UI or API server. `examples/stablematch_consumer.py` demonstrates how another Intelligent Contract can pin and consume a finalized matching hash.

## Repository layout

- `contracts/stablematch.py` — primary Intelligent Contract
- `reference/stablematch_model.py` — pure deterministic reference implementation
- `tests/unit/` — algorithmic invariant tests
- `tests/direct/` — prepared Direct Mode scenarios
- `fixtures/` — public demonstration evidence to publish after repo creation
- `docs/ARCHITECTURE.md` — protocol architecture
- `docs/SECURITY_MODEL.md` — threat model
- `docs/LIVE_TEST_PLAN.md` — exact 61999 live proof plan
- `STABLEMATCH_CODEX_MASTER_HANDOFF.txt` — final handoff instructions

## Local deterministic checks

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt -r requirements-test.txt
.venv/Scripts/python -m pytest tests/unit -q
.venv/Scripts/python scripts/preflight.py
.venv/Scripts/python -m compileall contracts reference tests scripts examples
```

Install the repository-local CLI and prepare the pinned stable GenVM SDK:

```bash
npm ci
.venv/Scripts/Activate.ps1
./scripts/prepare_stable_sdk.ps1
python -m pytest tests/direct -v -p no:cacheprovider
```

The Direct Mode SDK pin is GenVM `v0.2.16`, the official non-prerelease artifact containing the contract's declared SDK hash. `prepare_stable_sdk.ps1` validates against that stable SDK; it does not select the latest release. The test fixture uses the same explicit version. Do not use the v0.6 preview artifacts.

## Submission status

Local gates are recorded in `BUILD_STATUS.md`. The destination repository is `Ifem1/stablematch`; live deployment and lifecycle receipts remain blank until observed on Studionet 61999. See `docs/LIVE_TEST_PLAN.md` for the commit-pinned fixture and transaction sequence.
