# StableMatch architecture

StableMatch separates **semantic eligibility** from **deterministic allocation**.

## 1. Participants freeze the market

A market contains candidates and opportunities. Each candidate freezes:

- a public profile description (not treated as proof),
- one to four public HTTPS evidence URLs,
- an ordered preference list.

Each opportunity freezes:

- natural-language mandatory requirements,
- capacity,
- an ordered candidate preference list.

The market definition is hashed when sealed. No preference, requirement, source URL, profile, capacity, or membership may change afterwards.

## 2. GenLayer creates only eligibility edges

Only mutually listed candidate/opportunity pairs can be qualified. For each pair:

1. the leader independently fetches the candidate's sealed public evidence URLs;
2. the leader classifies the pair as `ELIGIBLE`, `NOT_ESTABLISHED`, `AMBIGUOUS`, or `UNAVAILABLE`;
3. validators independently fetch the same URLs and independently classify the pair;
4. decision classes must agree;
5. an `ELIGIBLE` proposal must carry grounded verbatim evidence that exists in the validator's own retrieved corpus and passes a second bounded evidence-sufficiency judgment.

`AMBIGUOUS` and `UNAVAILABLE` are non-terminal and may be retried during the qualification window. `ELIGIBLE` and `NOT_ESTABLISHED` are terminal for the sealed market.

## 3. Deterministic stable matching

Once every mutually acceptable pair has a terminal qualification receipt, `compute_matching` runs a candidate-proposing many-to-one Gale-Shapley algorithm.

GenLayer/LLMs do **not**:

- rank candidates;
- invent preferences;
- choose winners;
- choose capacities;
- break ties;
- calculate the assignment.

Those inputs are explicit and frozen. The algorithm consumes only frozen preferences, capacities, and `ELIGIBLE` edges.

## 4. Stability invariant

After matching, `blocking_pair_count(market_id)` recomputes whether any candidate/opportunity pair would both prefer each other to their assigned state and is semantically eligible. Finalization reverts if the blocking-pair count is non-zero.

That makes the contract's core claim testable:

> no mutually acceptable eligible blocking pair remains under the exact frozen preferences and capacities.

## 5. Composition

A downstream contract can pin both market ID and `matching_hash` and call:

```python
is_matched(market_id, candidate_id, opportunity_id, expected_matching_hash)
```

The matching hash commits to the sealed market definition and every final assignment.
