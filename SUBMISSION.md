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
