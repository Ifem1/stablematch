# StableMatch — standalone Intelligent Contract submission

## One-line purpose

StableMatch is a reusable two-sided matching primitive where GenLayer establishes semantic eligibility from public evidence and deterministic Gale-Shapley mechanics produce a stable assignment without allowing an LLM to rank or select winners.

## Why this is not a thin LLM wrapper

The nondeterministic output is only an eligibility edge. One semantic result cannot create an assignment.

A valid final market additionally requires:

- two independently authored preference sides;
- sealed capacities;
- immutable public evidence URLs;
- every mutually listed edge resolved;
- terminal fail-closed eligibility classes;
- deterministic candidate-proposing many-to-one Gale-Shapley;
- displacement handling;
- explicit final assignment state;
- matching-hash commitment;
- deterministic zero-blocking-pair verification.

## Consensus boundary

The leader fetches the candidate's sealed public evidence and proposes `ELIGIBLE`, `NOT_ESTABLISHED`, `AMBIGUOUS`, or `UNAVAILABLE`.

Validators independently fetch and independently classify. An eligible leader result must also include bounded verbatim evidence present in the validator's own corpus; the evidence bundle is independently judged against the frozen requirements.

Candidate profile text is not treated as proof.

## Deterministic boundary

GenLayer does not choose preferences, ranking, capacity, tie-breaking or winner selection. Once the graph of eligible mutually acceptable pairs is known, stable matching is deterministic.

## Reuse

Potential consumers include reviewer assignment, mentorship allocation, labour/task markets, agent/service matching, residency-style allocation, grants/reviewer allocation and any bounded two-sided market where semantic qualifications must be neutral but allocation rules should be explicit.

Downstream contracts can pin `matching_hash` and call `is_matched(...)`.

## Submission scope

No frontend. No backend authority. No hosted database. No off-chain matcher.

Canonical target is **Studionet 61999 only**.

## Response to the admission-control review request

The market owner registers directly and controls a draft-only, role-specific admission list for candidate registrars and opportunity registrars. Each list is bounded to 16 addresses. An unrelated address cannot add a candidate or opportunity unless the market owner admits it for that role; admitted registrars still own and seal their own records. This prevents an unrelated registration from blocking market sealing by withholding its seal.

The correction is deployed at `0x6a670925B2d44909C2E6C05771C53758f895A066` on Studionet chain ID 61999. The deployment transaction is `0x08c231742920a337d91a8ab7dddc7515ab06f978998aeccb1274e5f63f438a8c`. The live lifecycle exercised both admission roles with independent funded test addresses, completed a stable matching with `blocking_pair_count == 0`, confirmed an unavailable-evidence case remained sealed with no matching state, and confirmed a `NOT_ESTABLISHED` edge was excluded before matching. Repository tests also verify unadmitted registrations revert and only the owner may grant admission. Exact source identity and transaction receipts are in `docs/DEPLOYMENT.md`.
