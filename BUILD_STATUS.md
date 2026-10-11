# StableMatch build and live status

## Current source and deployment

- The admission-control correction is deployed on GenLayer Studionet, chain ID **61999**, at `0x6a670925B2d44909C2E6C05771C53758f895A066`.
- Deployment transaction: `0x08c231742920a337d91a8ab7dddc7515ab06f978998aeccb1274e5f63f438a8c`.
- Source commit used for deployment: `c13f48bbec4df56356f1089af5e0b1a4b6350789`; contract Git blob `3de0e75b5fd61b820018b70e94ded0c7551eefcc`.
- Deployed contract bytes equal the local source bytes; raw SHA-256 `3e92dae9a7e7f1840ab6e11ddfd7239a461cafd934e4af8fe057f9630779e1d1`; normalized UTF-8/LF SHA-256 `1ff3a1680d4aa0a9eaaf01a7c15083f179b160ee3380bd2408f9bb4c33c973cb`.
- Verified repository origin: `https://github.com/Ifem1/stablematch.git`.
- CLI: repository-local `genlayer@0.39.1`; RPC `https://studio.genlayer.com/api`; explorer `https://explorer-studio.genlayer.com`.

## Local verification

- Unit/property suite: **12 passed**.
- Direct Mode suite: **34 passed** using stable GenVM `v0.2.16`.
- GenVM lint: **3 checks passed**.
- GenLayer SDK semantic validation: **23 methods** (9 views, 14 writes).
- Python compileall: **passed**.
- Repository preflight: **passed**, with the normalized contract hash above.
- Generated comparisons: 250 contract-helper/reference markets and 500 independent reference/oracle markets.

## Admission-control correction

The market owner registers directly. While the market is draft, the owner can separately admit up to 16 candidate registrars and 16 opportunity registrars. Other addresses cannot register for a role unless admitted for that role. Admitted registrars own and seal their records. Direct Mode tests cover unadmitted registration rejection, owner-only admission, both registration roles, capacity limits and ownership behavior.

## Current live proof

- Market 1 exercised both role-specific admission lists with the three supplied test wallets. Six eligibility receipts were `ELIGIBLE`; Carol matched Security, Bob matched ML, and Alice remained unmatched. Matching hash `0351ef5bbdf1714d04ce9b944d090d89d0cf766d0b9ec3279214c955f473339e`; proposal count 5; blocking-pair count **0**.
- Market 2 returned `UNAVAILABLE` for a missing public fixture. Its matching transaction reached `FINALIZED`, but wrote no matching state; market readback remained `SEALED` with an empty matching hash. This confirms retryable unavailable evidence cannot create an assignment.
- Market 3 returned `NOT_ESTABLISHED` for a medical-license requirement unsupported by the pinned public fixture. The edge was excluded; candidate 5 remained unmatched, matching hash `788de71b58810c89854a1fe5f11e028121f421ccf6e93423f21479d3faef8f45`, and blocking-pair count **0**.
- Each signing stage independently checked CLI network information and canonical RPC `eth_chainId=0xf22f` before signing.
- Full lifecycle hashes, qualification receipts, source identity and readbacks are in `docs/DEPLOYMENT.md`.

## Architecture and security audit

- GenLayer consensus establishes eligibility from independently fetched public evidence; evidence excerpts must be literal substrings of a validator-fetched page.
- Preferences and capacities are explicit, participant-supplied and frozen before qualification.
- Assignment uses deterministic candidate-proposing many-to-one Gale-Shapley; the LLM does not rank candidates or calculate assignments.
- The known redirect/DNS-rebinding limitation remains documented as part of the external evidence-renderer trust boundary.
- StableMatch is contract-only: no frontend, backend authority or Docker dependency.

Earlier pre-admission deployment evidence remains in `docs/DEPLOYMENT.md` under its historical heading and does not identify the current deployment.
