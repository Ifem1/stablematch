# StableMatch security model

## Trust boundary

StableMatch does not decide whether a candidate is "best". It only adjudicates whether public evidence establishes a frozen set of mandatory requirements. Selection is deterministic after that point.

## Threats and mitigations

### Prompt injection in evidence

Public source content is treated as hostile data. Prompts explicitly forbid following source instructions. Candidate/opportunity definitions containing common control-instruction markers are rejected at registration. `ELIGIBLE` excerpts must be literal substrings of an individual validator-fetched page; whitespace normalization or concatenating separate pages cannot manufacture an excerpt.

Evidence URLs require HTTPS and syntactically valid public DNS hostnames. Credentials, private/local suffixes, IPv4 literals, shortened numeric IP forms, and dotted hexadecimal IP forms are rejected. This is URL-level validation: it cannot prove how every validator's network resolver handles DNS rebinding or redirects. The deployed GenLayer web renderer and its egress controls remain part of the trusted evidence-fetching boundary.

### Leader fabricates eligibility

A validator independently fetches the evidence and independently classifies the pair. The leader's class must match the validator's. For `ELIGIBLE`, every stored excerpt must exist in the validator's own retrieved corpus and the bundle must pass a second requirement-sufficiency judgment.

### Candidate self-claims become proof

The candidate profile is explicitly descriptive only. `ELIGIBLE` requires public evidence URLs; a candidate cannot qualify on profile text alone.

### Mutable preferences / strategic post-qualification edits

Candidates and opportunities seal themselves before the market seals. The market definition hash commits to both sides, requirements, capacities, evidence URLs and preference order. No edit path remains after sealing.

### Missing edge changes the result

Every pair that is mutually listed by both sides must resolve to a terminal `ELIGIBLE` or `NOT_ESTABLISHED` receipt before matching. `AMBIGUOUS`, `UNAVAILABLE`, and missing pairs fail closed.

### Stale qualification

Qualification is restricted to a bounded post-seal window, and matching must complete before that deadline. The live demo should use immutable commit-pinned GitHub evidence URLs.

### Algorithmic manipulation by LLM

The LLM never runs the matching algorithm and never produces rankings, capacities or tie breaks. Gale-Shapley is ordinary deterministic code.

### Unstable result

The finalized result is independently checked by the deterministic `blocking_pair_count` invariant. The write reverts if any blocking pair remains.

## Known limitations

- Stable matching is only as meaningful as the participant-supplied preference orders.
- `ELIGIBLE` means the sealed public evidence established the frozen requirements at qualification time; it is not identity proof or a permanent credential.
- The bounded market sizes are deliberate to keep deterministic execution reviewable on Studionet.
- URL validation blocks common private-address syntax but does not replace network-level redirect/DNS-rebinding controls in the evidence-fetching runtime.
- StableMatch does not prevent off-chain collusion or strategic preference reporting; it provides deterministic stability relative to the frozen submitted preferences.
