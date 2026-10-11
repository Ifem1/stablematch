# StableMatch build and live status

## Local verification (2026-10-11, admission correction)

- Exact extracted folder is a Git repository on `main`; origin is `https://github.com/Ifem1/stablematch.git`.
- Repository-local CLI is `genlayer@0.39.1`.
- Direct Mode pins stable GenVM `v0.2.16`; no v0.40 CLI or v0.6 preview SDK is used.
- Unit/property suite: **12 passed**.
- Direct Mode suite: **32 passed**.
- Python compileall: **passed**.
- Repository preflight: **passed**, UTF-8 LF-normalized contract SHA-256 `c391f8384ae04101f48af1c9d23b2dcea932dc85788c585e2c15acb27a7490d2`.
- GenVM lint: **3 checks passed**; SDK semantic validation passed for 21 methods (9 views, 12 writes).
- Generated comparisons: 250 contract-helper/reference markets plus 500 independent reference/oracle markets.
- Draft-market admission correction: the market owner registers directly; other addresses require role-specific owner admission before they can register a candidate or opportunity. Direct Mode confirms unadmitted registration fails and admitted records retain their participant owner.
- Updated local gates: unit suite **12 passed**; Direct Mode suite **34 passed**; compileall **passed**; stable SDK validation **23 methods** (9 views, 14 writes); GenVM lint **3 checks passed**.

## Studionet 61999 live proof

- Contract deployed at `0xB09Dc2259A3bf7788207421ADB7CB6c297913b6F` by `0x39680bd423437c0eaa18493629652821ec672c61`.
- Deployment transaction: `0x983de6124093dabf2411d495467307fe53509207044ec67e85c152e287d386de`.
- Source commit at deployment: `f680d3f8d5cfb3d5440462458ca433461adcbfa5`; deployed source returned by the canonical RPC was byte-for-byte equal to the contract at that commit.
- Flagship market 1: six `ELIGIBLE` receipts; Carol → Security, Bob → ML, Alice unmatched; blocking-pair count 0; matching hash `0dad5160a0e10e1fa45a019858dff08e9676b6049e1f1f51b842eb48cb8bb8ce`.
- Fail-closed market 2: unresolved `UNAVAILABLE` pair; matching attempt finalized with execution error; market remained sealed with no matching hash.
- Market 3: terminal `NOT_ESTABLISHED` edge was excluded; candidate remained unmatched and blocking-pair count was 0.
- Every signing stage checked CLI network info plus direct `eth_chainId=0xf22f` at the canonical RPC.
- Full deployment, transaction, receipt, assignment, and source-identity evidence is in `docs/DEPLOYMENT.md`.

## Security and architecture audit

- GenLayer consensus only classifies eligibility from independently fetched public evidence; evidence excerpts must be literal substrings of one validator-fetched page.
- Preferences and capacities are explicit, participant-supplied, and frozen before qualification.
- Assignment uses deterministic candidate-proposing many-to-one Gale-Shapley; the LLM does not rank or assign.
- The known redirect/DNS-rebinding limitation remains documented as part of the external evidence-renderer trust boundary.

The original deployment evidence and UTF-8 source-hash correction are recorded in `docs/DEPLOYMENT.md`; those values identify the pre-admission source only. The admission-corrected source is not yet claimed as deployed; its new address, source identity, and lifecycle evidence must be appended after canonical Studionet verification.
