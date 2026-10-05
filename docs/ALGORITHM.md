# Deterministic matching algorithm

StableMatch uses the candidate-proposing many-to-one Gale-Shapley algorithm after semantic eligibility has been frozen.

## Acceptable pair

A pair `(candidate, opportunity)` participates only when all three conditions hold:

1. the candidate explicitly ranked the opportunity;
2. the opportunity explicitly ranked the candidate;
3. the qualification receipt is `ELIGIBLE`.

Every other pair is unacceptable and cannot be a blocking pair.

## Proposal order

Candidates enter the proposal queue in registration order. Each candidate proposes down their own frozen ordered list. An opportunity holds up to its frozen capacity and always retains the candidates it ranks most highly among those that have proposed and are eligible.

When a more-preferred candidate arrives at a full opportunity, the currently worst-held candidate is displaced and returns to the queue.

## Termination

Each proposal advances that candidate's preference index. No candidate proposes to the same opportunity twice. With at most `C` candidates and at most `P` preferences per candidate, proposals are bounded by `C * P`.

The contract bounds `C <= 16` and `P <= 8`.

## Stability

A blocking pair exists only when:

- the pair is mutually listed and `ELIGIBLE`;
- the candidate prefers that opportunity to their current assignment (or is unmatched); and
- the opportunity either has unused capacity or prefers the candidate to at least one currently held candidate.

`blocking_pair_count` recomputes this condition over the frozen market after matching. `compute_matching` refuses to finalize if the count is non-zero.

## Candidate-optimality

For the standard many-to-one stable-marriage / college-admissions assumptions used here, candidate-proposing Gale-Shapley returns the candidate-optimal stable matching relative to the frozen acceptable-pair graph and the two submitted strict preference orders.

StableMatch does not claim truthful preference reporting is a dominant strategy for both sides, nor does it attempt to solve ties, couples, complementarities, quotas across groups, or unbounded matching markets. Those are intentionally outside this primitive.
