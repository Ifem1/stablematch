from reference.stablematch_model import (
    ELIGIBLE,
    NOT_ESTABLISHED,
    MatchingResult,
    blocking_pairs,
    stable_match,
    verify_stable,
)


def flagship_market():
    candidates = [1, 2, 3]
    opportunities = [10, 11]
    candidate_prefs = {
        1: [10, 11],  # Alice: Security, ML
        2: [10, 11],  # Bob: Security, ML
        3: [10, 11],  # Carol: Security, ML
    }
    opportunity_prefs = {
        10: [3, 1, 2],  # Security prefers Carol > Alice > Bob
        11: [2, 1, 3],  # ML prefers Bob > Alice > Carol
    }
    capacities = {10: 1, 11: 1}
    eligibility = {(c, o): ELIGIBLE for c in candidates for o in opportunities}
    return candidates, opportunities, candidate_prefs, opportunity_prefs, capacities, eligibility


def test_flagship_displacement_is_stable():
    args = flagship_market()
    result = stable_match(*args)
    assert result.candidate_match == {1: 0, 2: 11, 3: 10}
    assert set(result.opportunity_holds[10]) == {3}
    assert set(result.opportunity_holds[11]) == {2}
    assert blocking_pairs(result, *args) == []
    assert verify_stable(result, *args)


def test_ineligible_pair_is_skipped():
    candidates, opportunities, cp, op, caps, eligibility = flagship_market()
    eligibility[(3, 10)] = NOT_ESTABLISHED
    result = stable_match(candidates, opportunities, cp, op, caps, eligibility)
    assert result.candidate_match[1] == 10
    assert result.candidate_match[2] == 11
    assert result.candidate_match[3] == 0
    assert verify_stable(result, candidates, opportunities, cp, op, caps, eligibility)


def test_unlisted_candidate_is_unacceptable_to_opportunity():
    candidates = [1, 2]
    opportunities = [10]
    cp = {1: [10], 2: [10]}
    op = {10: [1]}  # opportunity deliberately does not list candidate 2
    caps = {10: 1}
    eligibility = {(1, 10): ELIGIBLE, (2, 10): ELIGIBLE}
    result = stable_match(candidates, opportunities, cp, op, caps, eligibility)
    assert result.candidate_match == {1: 10, 2: 0}
    assert verify_stable(result, candidates, opportunities, cp, op, caps, eligibility)


def test_capacity_two_keeps_two_best():
    candidates = [1, 2, 3, 4]
    opportunities = [10]
    cp = {cid: [10] for cid in candidates}
    op = {10: [4, 2, 3, 1]}
    caps = {10: 2}
    eligibility = {(cid, 10): ELIGIBLE for cid in candidates}
    result = stable_match(candidates, opportunities, cp, op, caps, eligibility)
    assert set(result.opportunity_holds[10]) == {4, 2}
    assert result.candidate_match[1] == 0
    assert result.candidate_match[3] == 0
    assert verify_stable(result, candidates, opportunities, cp, op, caps, eligibility)


def test_candidate_preference_matters():
    candidates = [1, 2]
    opportunities = [10, 11]
    cp = {1: [11, 10], 2: [10, 11]}
    op = {10: [1, 2], 11: [2, 1]}
    caps = {10: 1, 11: 1}
    eligibility = {(c, o): ELIGIBLE for c in candidates for o in opportunities}
    result = stable_match(candidates, opportunities, cp, op, caps, eligibility)
    assert result.candidate_match == {1: 11, 2: 10}
    assert verify_stable(result, candidates, opportunities, cp, op, caps, eligibility)


def test_blocking_pair_detector_catches_bad_manual_matching():
    candidates, opportunities, cp, op, caps, eligibility = flagship_market()
    bad = MatchingResult(
        candidate_match={1: 10, 2: 0, 3: 11},
        opportunity_holds={10: (1,), 11: (3,)},
        proposal_count=0,
    )
    blocks = blocking_pairs(bad, candidates, opportunities, cp, op, caps, eligibility)
    assert (3, 10) in blocks
    assert (2, 11) in blocks


def test_no_capacity_means_no_match():
    candidates = [1]
    opportunities = [10]
    cp = {1: [10]}
    op = {10: [1]}
    caps = {10: 0}
    eligibility = {(1, 10): ELIGIBLE}
    result = stable_match(candidates, opportunities, cp, op, caps, eligibility)
    assert result.candidate_match[1] == 0


def test_noneligible_status_never_blocks():
    candidates = [1, 2]
    opportunities = [10]
    cp = {1: [10], 2: [10]}
    op = {10: [2, 1]}
    caps = {10: 1}
    eligibility = {(1, 10): ELIGIBLE, (2, 10): NOT_ESTABLISHED}
    result = stable_match(candidates, opportunities, cp, op, caps, eligibility)
    assert result.candidate_match == {1: 10, 2: 0}
    assert blocking_pairs(result, candidates, opportunities, cp, op, caps, eligibility) == []


def test_candidate_proposing_result_is_candidate_optimal_among_stable_matchings():
    from itertools import permutations

    candidates = [1, 2, 3]
    opportunities = [10, 11, 12]
    cp = {
        1: [10, 11, 12],
        2: [11, 12, 10],
        3: [12, 10, 11],
    }
    op = {
        10: [2, 3, 1],
        11: [3, 1, 2],
        12: [1, 2, 3],
    }
    caps = {oid: 1 for oid in opportunities}
    eligibility = {(cid, oid): ELIGIBLE for cid in candidates for oid in opportunities}
    result = stable_match(candidates, opportunities, cp, op, caps, eligibility)

    stable_results = []
    for assignment in permutations(opportunities):
        match = dict(zip(candidates, assignment))
        holds = {oid: tuple(cid for cid in candidates if match[cid] == oid) for oid in opportunities}
        candidate_result = MatchingResult(match, holds, 0)
        if verify_stable(candidate_result, candidates, opportunities, cp, op, caps, eligibility):
            stable_results.append(candidate_result)

    assert stable_results
    for candidate in candidates:
        result_rank = cp[candidate].index(result.candidate_match[candidate])
        assert all(cp[candidate].index(stable.candidate_match[candidate]) >= result_rank for stable in stable_results)
