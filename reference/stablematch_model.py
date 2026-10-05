"""Pure-Python deterministic reference model for StableMatch.

The on-chain contract uses the same candidate-proposing many-to-one Gale-Shapley
mechanics. This model is intentionally independent of GenLayer so matching
invariants can be tested exhaustively and cheaply.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple

ELIGIBLE = 1
NOT_ESTABLISHED = 2
AMBIGUOUS = 3
UNAVAILABLE = 4


@dataclass(frozen=True)
class MatchingResult:
    candidate_match: Dict[int, int]
    opportunity_holds: Dict[int, Tuple[int, ...]]
    proposal_count: int


def _rank(order: Sequence[int], candidate_id: int) -> int:
    try:
        return order.index(candidate_id)
    except ValueError:
        return 10**9


def stable_match(
    candidate_ids: Sequence[int],
    opportunity_ids: Sequence[int],
    candidate_preferences: Mapping[int, Sequence[int]],
    opportunity_preferences: Mapping[int, Sequence[int]],
    capacities: Mapping[int, int],
    eligibility: Mapping[Tuple[int, int], int],
) -> MatchingResult:
    """Run deterministic candidate-proposing many-to-one Gale-Shapley.

    Only pairs with status ``ELIGIBLE`` are acceptable. Every ordering is
    supplied explicitly by the market participants and frozen before matching;
    the algorithm performs no semantic ranking.
    """
    valid_opps = set(opportunity_ids)
    next_index = {cid: 0 for cid in candidate_ids}
    match = {cid: 0 for cid in candidate_ids}
    holds: Dict[int, List[int]] = {oid: [] for oid in opportunity_ids}
    queue = list(candidate_ids)
    proposals = 0

    while queue:
        cid = queue.pop(0)
        prefs = list(candidate_preferences.get(cid, ()))
        accepted = False

        while next_index[cid] < len(prefs):
            oid = prefs[next_index[cid]]
            next_index[cid] += 1
            proposals += 1

            if oid not in valid_opps:
                continue
            if eligibility.get((cid, oid)) != ELIGIBLE:
                continue
            if cid not in opportunity_preferences.get(oid, ()):
                continue

            cap = int(capacities.get(oid, 0))
            if cap <= 0:
                continue

            current = holds[oid]
            if len(current) < cap:
                current.append(cid)
                match[cid] = oid
                accepted = True
                break

            ranks = opportunity_preferences.get(oid, ())
            worst = max(current, key=lambda held: _rank(ranks, held))
            if _rank(ranks, cid) < _rank(ranks, worst):
                current.remove(worst)
                current.append(cid)
                match[worst] = 0
                queue.append(worst)
                match[cid] = oid
                accepted = True
                break

        if not accepted:
            match[cid] = 0

    frozen_holds = {oid: tuple(holds[oid]) for oid in opportunity_ids}
    return MatchingResult(match, frozen_holds, proposals)


def blocking_pairs(
    result: MatchingResult,
    candidate_ids: Sequence[int],
    opportunity_ids: Sequence[int],
    candidate_preferences: Mapping[int, Sequence[int]],
    opportunity_preferences: Mapping[int, Sequence[int]],
    capacities: Mapping[int, int],
    eligibility: Mapping[Tuple[int, int], int],
) -> List[Tuple[int, int]]:
    """Return every mutually acceptable blocking pair."""
    blocks: List[Tuple[int, int]] = []
    valid_opps = set(opportunity_ids)

    for cid in candidate_ids:
        assigned = result.candidate_match.get(cid, 0)
        prefs = list(candidate_preferences.get(cid, ()))
        assigned_rank = prefs.index(assigned) if assigned in prefs else len(prefs) + 1

        for index, oid in enumerate(prefs):
            if index >= assigned_rank:
                break
            if oid not in valid_opps:
                continue
            if eligibility.get((cid, oid)) != ELIGIBLE:
                continue
            opp_prefs = list(opportunity_preferences.get(oid, ()))
            if cid not in opp_prefs:
                continue

            current = list(result.opportunity_holds.get(oid, ()))
            cap = int(capacities.get(oid, 0))
            if len(current) < cap:
                blocks.append((cid, oid))
                continue

            worst = max(current, key=lambda held: _rank(opp_prefs, held))
            if _rank(opp_prefs, cid) < _rank(opp_prefs, worst):
                blocks.append((cid, oid))

    return blocks


def verify_stable(*args, **kwargs) -> bool:
    result = args[0] if args else kwargs["result"]
    rest = args[1:] if args else ()
    if rest:
        return blocking_pairs(result, *rest) == []
    return blocking_pairs(
        result,
        kwargs["candidate_ids"],
        kwargs["opportunity_ids"],
        kwargs["candidate_preferences"],
        kwargs["opportunity_preferences"],
        kwargs["capacities"],
        kwargs["eligibility"],
    ) == []
