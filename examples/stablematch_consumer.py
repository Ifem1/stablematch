# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
"""Minimal composition example. Not a frontend and not an authority backend."""
from genlayer import *


@gl.contract_interface
class IStableMatchRead:
    class View:
        def is_matched(self, market_id: u256, candidate_id: u256, opportunity_id: u256, expected_matching_hash: str) -> bool: ...


class StableMatchConsumer(gl.Contract):
    stablematch: Address

    def __init__(self, stablematch: Address):
        self.stablematch = stablematch

    @gl.public.view
    def assignment_is_valid(self, market_id: u256, candidate_id: u256, opportunity_id: u256, expected_matching_hash: str) -> bool:
        return bool(
            gl.get_contract_at(IStableMatchRead, self.stablematch).view().is_matched(
                market_id, candidate_id, opportunity_id, expected_matching_hash
            )
        )
