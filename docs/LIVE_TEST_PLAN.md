# StableMatch 61999 live lifecycle plan

**Network lock:** Studionet only, chain ID **61999**, RPC `https://studio.genlayer.com/api`.

Do not use Studio-dev. Do not use chain 61997.

## Tooling

Use repository-local `genlayer@0.39.1` only:

```bash
npm install
npm run genlayer -- --version
npm run genlayer -- network set studionet
npm run genlayer -- network info
```

Before every signing/deployment stage, independently verify the active RPC and chain ID are the values in `NETWORK_LOCK.json`.

## Fixture preparation

The canonical fixture source is pinned to repository commit `71c7d5803627dfa3083b4a22ab9db7f888427982`:

- Alice: `https://raw.githubusercontent.com/Ifem1/stablematch/71c7d5803627dfa3083b4a22ab9db7f888427982/fixtures/candidate_alice.txt`
- Bob: `https://raw.githubusercontent.com/Ifem1/stablematch/71c7d5803627dfa3083b4a22ab9db7f888427982/fixtures/candidate_bob.txt`
- Carol: `https://raw.githubusercontent.com/Ifem1/stablematch/71c7d5803627dfa3083b4a22ab9db7f888427982/fixtures/candidate_carol.txt`

Do not use `main` for the canonical live proof. These raw URLs were fetched successfully (HTTP 200); the commit SHA pins the public evidence contents.

## Flagship market

Create one market with two capacity-1 opportunities:

1. **Security review** — mandatory public evidence of Python engineering and production security-review experience.
2. **ML review** — mandatory public evidence of Python engineering and ML systems experience.

Register Alice, Bob and Carol. Give all three candidate preferences:

`Security > ML`

Give opportunity preferences:

- Security: `Carol > Alice > Bob`
- ML: `Bob > Alice > Carol`

All three public fixtures intentionally satisfy both requirement sets.

Expected candidate-proposing stable matching:

- Carol -> Security
- Bob -> ML
- Alice -> unmatched

The important algorithmic event is displacement: Alice is initially held by Security, then Carol displaces Alice; Bob eventually occupies ML; Alice has no blocking pair.

## Required live proof

Capture full transaction hashes and final states for:

1. deployment;
2. market creation;
3. both opportunity registrations;
4. all candidate registrations;
5. every evidence-source registration;
6. preference freezing;
7. candidate/opportunity sealing;
8. market sealing and definition hash;
9. all six mutually listed eligibility writes;
10. `compute_matching`;
11. readback of every candidate match;
12. `blocking_pair_count == 0`;
13. matching hash pinning;
14. negative `is_matched` read using a wrong hash;
15. positive `is_matched` reads using the correct hash.

## Fail-closed live proof

Create a second small market where one mutually listed pair remains `AMBIGUOUS` or `UNAVAILABLE` and prove `compute_matching` cannot execute.

Also prove a `NOT_ESTABLISHED` edge is terminal and simply removed from the acceptable graph rather than being treated as eligible.

## Evidence record

After live execution, write exact values into `docs/DEPLOYMENT.md`:

- repository HEAD;
- contract Git blob;
- normalized contract SHA-256;
- deployed source hash returned by StudioNet;
- contract address;
- full deployment transaction;
- full lifecycle transactions;
- definition hash;
- all qualification receipt hashes/classes;
- final matching hash;
- final assignments;
- blocking-pair count;
- Direct Mode / lint / preflight counts.
