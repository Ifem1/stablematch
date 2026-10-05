"""Seeded property-style tests for the deterministic reference matcher."""

import random

from reference.stablematch_model import ELIGIBLE, NOT_ESTABLISHED, blocking_pairs, stable_match


def contract_algorithm(candidate_ids, opportunity_ids, cp, op, capacities, eligibility):
    """Independent transcription of the bounded on-chain proposal loop."""
    queue = list(candidate_ids)
    next_index = {cid: 0 for cid in candidate_ids}
    match = {cid: 0 for cid in candidate_ids}
    holds = {oid: [] for oid in opportunity_ids}
    proposals = 0
    while queue:
        cid = queue.pop(0)
        accepted = False
        while next_index[cid] < len(cp[cid]):
            oid = cp[cid][next_index[cid]]
            next_index[cid] += 1
            proposals += 1
            if oid not in holds or cid not in op[oid] or eligibility.get((cid, oid)) != ELIGIBLE:
                continue
            current = holds[oid]
            rank = {candidate: i for i, candidate in enumerate(op[oid])}
            if len(current) < capacities[oid]:
                current.append(cid)
                match[cid] = oid
                accepted = True
                break
            worst = max(current, key=lambda held: rank.get(held, 1_000_000))
            if rank.get(cid, 1_000_000) < rank.get(worst, 1_000_000):
                current.remove(worst)
                current.append(cid)
                match[worst] = 0
                queue.append(worst)
                match[cid] = oid
                accepted = True
                break
        if not accepted:
            match[cid] = 0
    return match, {oid: tuple(members) for oid, members in holds.items()}, proposals


def test_seeded_random_markets_have_no_blocking_pairs_and_respect_capacity():
    rng = random.Random(0x5A7B1E)
    for _case in range(250):
        n_candidates = rng.randint(1, 8)
        n_opportunities = rng.randint(1, 5)
        candidates = list(range(1, n_candidates + 1))
        opportunities = list(range(100, 100 + n_opportunities))

        cp = {}
        for cid in candidates:
            prefs = opportunities[:]
            rng.shuffle(prefs)
            keep = rng.randint(1, len(prefs))
            cp[cid] = prefs[:keep]

        op = {}
        for oid in opportunities:
            prefs = candidates[:]
            rng.shuffle(prefs)
            keep = rng.randint(1, len(prefs))
            op[oid] = prefs[:keep]

        capacities = {oid: rng.randint(1, min(3, n_candidates)) for oid in opportunities}
        eligibility = {}
        for cid in candidates:
            for oid in opportunities:
                eligibility[(cid, oid)] = ELIGIBLE if rng.random() < 0.72 else NOT_ESTABLISHED

        result = stable_match(candidates, opportunities, cp, op, capacities, eligibility)

        assert blocking_pairs(result, candidates, opportunities, cp, op, capacities, eligibility) == []
        for oid in opportunities:
            assert len(result.opportunity_holds[oid]) <= capacities[oid]
        for cid in candidates:
            oid = result.candidate_match[cid]
            if oid:
                assert oid in cp[cid]
                assert cid in op[oid]
                assert eligibility[(cid, oid)] == ELIGIBLE


def test_determinism_same_inputs_same_outputs():
    rng = random.Random(1337)
    candidates = list(range(1, 9))
    opportunities = [10, 11, 12]
    cp = {}
    op = {}
    for cid in candidates:
        prefs = opportunities[:]
        rng.shuffle(prefs)
        cp[cid] = prefs
    for oid in opportunities:
        prefs = candidates[:]
        rng.shuffle(prefs)
        op[oid] = prefs
    caps = {10: 2, 11: 2, 12: 2}
    eligibility = {(cid, oid): ELIGIBLE for cid in candidates for oid in opportunities}
    first = stable_match(candidates, opportunities, cp, op, caps, eligibility)
    second = stable_match(candidates, opportunities, cp, op, caps, eligibility)
    assert first == second


def test_reference_matches_contract_loop_on_bounded_generated_markets():
    rng = random.Random(0x61999)
    for _case in range(500):
        candidates = list(range(1, rng.randint(2, 8) + 1))
        opportunities = list(range(100, 100 + rng.randint(1, 5)))
        cp = {}
        for cid in candidates:
            prefs = opportunities[:]
            rng.shuffle(prefs)
            cp[cid] = prefs[: rng.randint(1, len(prefs))]
        op = {}
        for oid in opportunities:
            prefs = candidates[:]
            rng.shuffle(prefs)
            op[oid] = prefs[: rng.randint(1, len(prefs))]
        capacities = {oid: rng.randint(1, min(3, len(candidates))) for oid in opportunities}
        eligibility = {
            (cid, oid): ELIGIBLE if rng.random() < 0.7 else NOT_ESTABLISHED
            for cid in candidates
            for oid in opportunities
        }
        reference = stable_match(candidates, opportunities, cp, op, capacities, eligibility)
        contract = contract_algorithm(candidates, opportunities, cp, op, capacities, eligibility)
        assert reference.candidate_match == contract[0]
        assert reference.opportunity_holds == contract[1]
        assert reference.proposal_count == contract[2]
        assert blocking_pairs(reference, candidates, opportunities, cp, op, capacities, eligibility) == []
