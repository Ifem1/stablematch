# StableMatch Studionet deployment evidence

## Deployment identity

- Network: GenLayer Studionet, chain ID **61999**.
- Canonical RPC: `https://studio.genlayer.com/api`.
- Explorer: `https://explorer-studio.genlayer.com`.
- Repository: [`Ifem1/stablematch`](https://github.com/Ifem1/stablematch).
- Repository HEAD used for deployment: `f680d3f8d5cfb3d5440462458ca433461adcbfa5`.
- Contract Git blob at that HEAD: `c40ed5715510267bd4556ea13b60761b2ab5eae6`.
- Deployer: `0x39680bd423437c0eaa18493629652821ec672c61`.
- Contract address: `0xB09Dc2259A3bf7788207421ADB7CB6c297913b6F`.
- Deployment transaction: `0x983de6124093dabf2411d495467307fe53509207044ec67e85c152e287d386de` (receipt `ACCEPTED`, consensus result `MAJORITY_AGREE`).
- Deployed-source identity: `gen_getContractCode` returned source bytes exactly equal to `contracts/stablematch.py` at the deployment HEAD. Raw source SHA-256 and LF-normalized UTF-8 SHA-256: `c391f8384ae04101f48af1c9d23b2dcea932dc85788c585e2c15acb27a7490d2`.
- The repository preflight now specifies UTF-8 explicitly so its source hash is reproducible across operating systems. The deployed-source comparison was performed directly against the canonical RPC.

Before every signing/deployment transaction, the repository-local CLI reported Studionet/61999 and the canonical RPC, and a direct `eth_chainId` query to that RPC returned `0xf22f` (61999). The transaction below was sent only after those checks. Live evidence fixtures use commit-pinned raw GitHub URLs from `71c7d5803627dfa3083b4a22ab9db7f888427982`.

## Local verification

- Unit/property suite: **12 passed**.
- Direct Mode suite: **32 passed**, pinned stable GenVM `v0.2.16`.
- GenVM lint: **3 checks passed**.
- GenVM SDK semantic validation: **passed**, StableMatch with 21 methods (9 views, 12 writes).
- Python compileall: **passed**.
- Repository preflight: **passed**, UTF-8 LF-normalized contract SHA-256 `c391f8384ae04101f48af1c9d23b2dcea932dc85788c585e2c15acb27a7490d2`.
- Repository-local CLI: `genlayer@0.39.1`.

## Flagship market 1

- Definition hash: `3f9b8ccb2395eaadb02612588c43b6b007402a3fe6a3cd181c09f84080b1a1f2`.
- Matching hash: `0dad5160a0e10e1fa45a019858dff08e9676b6049e1f1f51b842eb48cb8bb8ce`.
- Final assignments: Alice (candidate 1) → unmatched; Bob (candidate 2) → ML (opportunity 2); Carol (candidate 3) → Security (opportunity 1).
- `blocking_pair_count(1)`: **0**; proposal count: **5**.
- Composition readbacks: `is_matched(1, 3, 1, matching_hash)` → `true`; same call with 64 zeroes as the expected hash → `false`.

### Flagship transaction hashes

| Step | Transaction hash |
|---|---|
| Create market 1 | `0x872507c8970c2607eb0bcca44fb57d91f3dbfa90e4e045aa12f7400e32111cc0` |
| Register Security opportunity 1 | `0xe47bd75ada47ab98298cb2dbc018a83072357aa60a3c94fbcb845aa472428f46` |
| Register ML opportunity 2 | `0x8ea36f19954414dd4fd13914f6466a20f41773ea0c2607d865d0e46f25ef41fc` |
| Register Alice candidate 1 | `0x91646a497f6a9a2c7a2601dc0952ecde92e074e045c7dff22bcde6bfde81ded3` |
| Register Bob candidate 2 | `0xa8473424cba4c0db49ce5d8ca636bb75e38b2b466b73c2df66acb97ab2d950f5` |
| Register Carol candidate 3 | `0x821d943121de7de35eae25976745b8df2ed97801ea45544076745850ec412bb9` |
| Add Alice pinned source | `0x459d7719be52db881acf3c82a134a3851d1d28b5d2416f27e1a4d4de6563b8cf` |
| Add Bob pinned source | `0x11ffd367076031044516913236fbc270735c99d83f754b84d54ea28ba2237a22` |
| Add Carol pinned source | `0xaa8137d8f95f49afec008909d94e2904f118286a781be050b69a83fec216a4c0` |
| Freeze Alice preferences `[1, 2]` | `0xca83976a1a9ecfdc2cf0248e4bb9b44adfd174a98023979a03653f8adb70f4b6` |
| Freeze Bob preferences `[1, 2]` | `0xd595b27563a3f14206d26a7b1d81defdeaad9b68ccba5d88cce9e87bb811d291` |
| Freeze Carol preferences `[1, 2]` | `0xcf1d1bdb06d8a976e1c672f5b462b35bc721efb8dfedeb71cb8910a589d7e89a` |
| Freeze Security preferences `[3, 1, 2]` | `0x2c9f4b38fc2237b6c691643d35650ae9d3f588a98cf4e5ec270c648208414635` |
| Freeze ML preferences `[2, 1, 3]` | `0xd0374d6d37cceedeb4df12ff42bc99273259589c3430d5898683850bc9af636a` |
| Seal Alice | `0x3565e1f0c1fadeedde3675c6e22de77d0fc5199fca2e6e0f088dcca0c66cea14` |
| Seal Bob | `0x305516711ff6b7fce0e0e1c7f88febd973aaab11499836580c2443559fa8d9c4` |
| Seal Carol | `0x4edbafb53bc70f87b63bd40260c83b8c26d750dd36d9472be432271625428d49` |
| Seal Security | `0x3ffd9680f6ddb6ca0d83925198ec0d3914cef67fdfd4abdd7918e1acdb9a9530` |
| Seal ML | `0x7fe7f145729f918d83188d9235cce794a25612c73f6226e27729756d5a4fa357` |
| Seal market 1 | `0x59fcd784ca6580c4cc453e7bd55bb7f47623a2337537f59403bf4c07eb473b38` |
| Qualify Alice → Security | `0x2d00dd0c66dbe5f9d0d6f2f29c6863f4dbf3f4631c564dee1ad2c17590c40fae` |
| Qualify Alice → ML | `0x721823df640a2d600a75417eab33503e997a537bd3ed74addc47963ee7127d34` |
| Qualify Bob → Security | `0x2978f8b7329559fde8318a96f5c242b74baaee24a61106d3a2eb72f566ed4c80` |
| Qualify Bob → ML | `0xaa733ddfa05091fd24ff2ed187cfc51f434e306f7fa5966717caaa04dba34ece` |
| Qualify Carol → Security | `0x9ff3065e4e44cb4e01f34c048a255deff61da0e924e3e4640ee2d4fa0d5a27d2` |
| Qualify Carol → ML | `0x4d15b635c8dfab07b0ab060515ca647bbb08fffa5a260da26fa6b8fccd1c9d15` |
| Compute matching 1 | `0x14c5d78fd12237805fd21cb61df6237efbd0fd56dfd10f86f0708bcc91cf17d3` |

### Qualification receipts

| Pair | Status | Pair receipt hash |
|---|---|---|
| Alice 1 → Security 1 | `ELIGIBLE` | `ab4543c40dcdcec2e6a64c032d91546dcf0e28f55bf112a2931a8ba43a09033f` |
| Alice 1 → ML 2 | `ELIGIBLE` | `d073ff09414dec75538095ec10e64f2a6024c75d9b022d5901996ad86f785bf8` |
| Bob 2 → Security 1 | `ELIGIBLE` | `ce3e3e7f925162e3dd60d20b03b8be8a4c6d8eedf438a32ee430ac62715f884f` |
| Bob 2 → ML 2 | `ELIGIBLE` | `75beef44b76f0b3b9621df60d0cb02190a80c852f812424239aed2b0fcb200b3` |
| Carol 3 → Security 1 | `ELIGIBLE` | `03f31c638f81342d1fa6793d98ff44842b37510fe6d5b427fb5d0318f843dc0e` |
| Carol 3 → ML 2 | `ELIGIBLE` | `7b8575e281216687ec26c39ff541d47ecec788fcf8d6258f05e089b9104a98fe` |

## Fail-closed market 2

Market 2 used a mutually listed candidate 4 / opportunity 3 pair and a commit-pinned raw GitHub path for a nonexistent fixture. Qualification transaction `0xbea9c771176e8abaeebb351a1cbe7cca48eeb58b86a33b114a61579bcc538d56` produced `UNAVAILABLE` (status 4), empty evidence, pair hash `cb564bebe47b4fd0eb9de25a092eb66c79f18693367ef9c4abd2530af876d832`. The `compute_matching(2)` attempt `0x0e6ad273405f65a77b34a8b134602b2e7f9ebfedb1f694652298e7a8e2082cfd` finalized with leader execution result `ERROR`; readback remained `SEALED`, matching hash empty, candidate 4 unmatched. No matching state was written.

Market 2 setup transactions: create `0xc38733046ab79a73ea7b201cdf07a6bc4e31e462d60280651b4da8bbed4ec825`; register opportunity 3 `0xff265a7044267f956e308129fa5c1163193ba4459091ff7f10a827faae81687a`; register candidate 4 `0x8e37df96f8d7a8fee4e5336572de066562268133471d7678bc73c26ea045521f`; add unavailable source `0x0dc7fae38e5964beccc448ca996bbe97c5d4dbf308073c915597559574bba573`; candidate preferences `0xad27af8edd2cd59968f7474044c2a37854b6f526acd190ad46db06c118e2703a`; opportunity preferences `0xa1352d807e55ff0942c9601db3b98f37e86460801730d24db26ca183d7c14aa7`; seal candidate `0x01db51c85804790d62347dcc527180c9dfddb780e9335f23e40b4d4c575d727f`; seal opportunity `0x9bb7ace7b9290d91c1b4e259779076e5a8d945f8e551b1b9efd2e44d98d0e631`; seal market `0xbaa94df06540202b400782bdcf189a68193c731107a1c2877d084673d9b0dad0`.

## NOT_ESTABLISHED graph-exclusion market 3

Market 3 definition hash: `0e011eddcf5fd0c1d8c7652646516790b40228db4451c13123b97e48e1ab666e`. Candidate 5 / opportunity 4 were mutually listed; the pinned Bob fixture did not establish the law-degree requirement. Qualification transaction `0xd3f94ef9e40db15bb81e43520698821485790ab1ddab5eab3d283e7ee694f801` produced `NOT_ESTABLISHED` (status 2), empty evidence, pair hash `6c66c1d7a16c51f1f6ae608b66cd4b52757041c788f274f532761fedd842c479`. Matching transaction `0x31143e163ccf49ab52502cf8053c67c895a5867fde220241be310fd25426c2a6` finalized the market with candidate 5 unmatched, matching hash `655222315edb50fd2b08d7a9a8109e50551dc007c20479d45878c7b62dbdb37d`, and blocking-pair count **0**.

Market 3 setup transactions: create `0x3716db560cdee9d254271fe2940f36fe67c81306500e40b5f95ccccd9e10de75`; register opportunity 4 `0xa468a2c4d264f1d00e9f69fe5b988e8a82e1c1ea045e7e07e775275a666c059a`; register candidate 5 `0xd60b1d8f3bbcf336f87dc819609feb65d7d4262c6a471b8597bc45f620ae8d4f`; add pinned source `0x4f7eaa5160dc47628f169985e16939983a238ea2fd70d0b3d5ce32cf2316be36`; candidate preferences `0x189b39d123f3af747bbd0f25f9965327bcae24f23e96a1ac4b77b612bc89d002`; opportunity preferences `0xc3880f8d454389601518af84e95acd4bfbccce8f7d6d8052b5c7bdef5ee6486e`; seal candidate `0x22b30f2b0871fbe42a879df14191c4ef993d8ddbc5ebde6a566051db6595c58d`; seal opportunity `0xe2ac47ed17ca299af1d7b44ec337ebef0b6bb794059e682faf3e45dcaa7dbc93`; seal market `0x65a22480a85ea64372a91a9f3ce3a2f74efa3f74c7eb66449da57de341855dbc`.

## Scope and limitations

This is a Studionet demonstration, not identity proof or a permanent credential. The evidence sources are public demo fixtures. The deployed contract is byte-for-byte the committed contract; the LLM determined eligibility classes only, while the frozen participant rankings and deterministic matching code produced the assignments. The documented DNS rebinding and redirect-egress limitation remains part of the evidence-renderer trust boundary.
