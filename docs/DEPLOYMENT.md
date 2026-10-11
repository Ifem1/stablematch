# StableMatch Studionet deployment evidence

## Corrected deployment (2026-10-11)

The admission-control correction is committed and pushed to `Ifem1/stablematch` at source commit `c13f48bbec4df56356f1089af5e0b1a4b6350789` (fix commit `832850b3c81c6469592fc627cc6bcd59ea5a1849`). Contract Git blob: `3de0e75b5fd61b820018b70e94ded0c7551eefcc`. The repository preflight normalized contract SHA-256 is `1ff3a1680d4aa0a9eaaf01a7c15083f179b160ee3380bd2408f9bb4c33c973cb`; StudioNet returned source bytes exactly equal to the local contract (raw SHA-256 `3e92dae9a7e7f1840ab6e11ddfd7239a461cafd934e4af8fe057f9630779e1d1`, 53,829 bytes).

- Network: Studionet, chain ID **61999**; RPC `https://studio.genlayer.com/api`; explorer `https://explorer-studio.genlayer.com`.
- CLI: repository-local `genlayer@0.39.1`.
- Deployer: `0xd6423ae82a975d55c6ceac222827a727325e0459`.
- Corrected contract: `0x6a670925B2d44909C2E6C05771C53758f895A066`.
- Deployment transaction: `0x08c231742920a337d91a8ab7dddc7515ab06f978998aeccb1274e5f63f438a8c` (accepted, `MAJORITY_AGREE`).

Before deployment and each signed lifecycle write, the local CLI network settings and a direct `eth_chainId` RPC read were checked; the latter returned `0xf22f` (61999). No other network was used. The source identity is tied to the commit above, while the documentation commit is later because it records the resulting deployment and live receipts.

Local verification for this source: 12 unit/property tests, 34 Direct Mode tests, 3 GenVM lint checks, SDK validation for 23 methods (9 views / 14 writes), Python compileall, and repository preflight all passed.

### Admission and matching live proof — market 1

Market 1 was created by the market owner, who admitted candidate registrar A (`0x39680bd423437c0eaa18493629652821ec672c61`) and registrar B (`0xa49c51d759790116d451f256654dd9f0549d341f`) separately for candidate and opportunity registration. The market owner registered Alice; A registered Bob and Security; B registered Carol and ML. Each participant sealed their own record. This exercises both role-specific admission lists with the three user-provided funded test wallets. Candidate evidence used commit-pinned raw fixtures: Alice `https://raw.githubusercontent.com/Ifem1/stablematch/71c7d5803627dfa3083b4a22ab9db7f888427982/fixtures/candidate_alice.txt`, Bob `https://raw.githubusercontent.com/Ifem1/stablematch/71c7d5803627dfa3083b4a22ab9db7f888427982/fixtures/candidate_bob.txt`, and Carol `https://raw.githubusercontent.com/Ifem1/stablematch/71c7d5803627dfa3083b4a22ab9db7f888427982/fixtures/candidate_carol.txt`.

- Market ID: `1`; status: `MATCHED`; definition hash: `164f35e558c3b95def84c09ce43461b235469425877573ae1c6098ec0e143f31`.
- Matching hash: `0351ef5bbdf1714d04ce9b944d090d89d0cf766d0b9ec3279214c955f473339e`; proposal count: `5`; blocking-pair count: **0**.
- Assignments: Alice (candidate 1) → unmatched; Bob (candidate 2) → ML (opportunity 2); Carol (candidate 3) → Security (opportunity 1). Readback showed opportunity 1 holds `[3]` and opportunity 2 holds `[2]`.
- Composition readback: `is_matched(1,3,1,<matching hash>)` returned true; the same query with the all-zero hash returned false.

| Lifecycle operation | Transaction hash |
|---|---|
| Create market 1 | `0xf7d8683d623e7489ddb7f78371044ab6382e04cfd6c3301a130f98e8945d079d` |
| Admit A as candidate registrar | `0x1462a1bb4271675d7352f5adeb6df8d31b9612027eea4a0fe680c99569e9665f` |
| Admit B as candidate registrar | `0x8a9eef7138317ef9f5b4caa6d1ea58185814c23c5863195b19b14a6532cd95f3` |
| Admit A as opportunity registrar | `0xeb131be1948d11facef053489ac5d088320c689c4a73a7e6c43e703906de94b4` |
| Admit B as opportunity registrar | `0x9a17764a1839d2144f8e8b31e04c4349f5eb382ad9393a03df2999e4dbfbc5f3` |
| Register Alice, Security, Bob, ML, Carol | `0xf842d15a67eb3b2f7f22ec8289c8f692632e9ac7308c65e69b92387c6a765faf`; `0x8bfc97d2ee27a35a4ce35f252c8ead9acb9b58f5f24d0531a8871a557d8e43a3`; `0x87d647836a67d55f1c1e933b29486c4045e92a9ae0fb2454f80b576dc3d0ac64`; `0xcacc57c075cf66ae5bad8f70b33061247e3fbba0276f2bf43ca783a51e823628`; `0x7ffcd39f51b1c30362bed6eb675a494f7aa6b5e468d7b637285e81db6669ad01` |
| Register Alice, Bob, Carol pinned sources | `0x2ad258f9be14196c67fa0aea7a1a5dd33ab208b21e08d14f8500531591d6aa7a`; `0xc54c0c54cfd39676a888341f3a292e2c226d2edb5eb546d79c4344a4962b63ab`; `0xcd8baa915f2b4690b1123f09ac06b498df5e625b91378138c9c4c7ae6390ec9e` |
| Freeze candidate preferences | `0xdce936866a7e3c65bfe6a8b221ef74418b4485493e30442a3edc277e74502a29`; `0x942009ee2e3a8fd40160c70268dc30f88f005240a6a17b44825177e8f97bba0f`; `0x4b5a1c26322710ae4e4f75e28c2b3bf506d8aae2bedf4f97b56abae8693941ab` |
| Seal Alice, Bob, Carol | `0xab7d927b631f36b50da81ce1f9f4fd8c559444d99ad145df9348ee26e7d4aef2`; `0x4e376b08398d4048fdddf1605aeb209cacc9c567fb6c53f282fd31afef01ef4c`; `0x7bb204f9597b3c794f6a5da452c196b7367dd3119f8f7e35bc69d589e45ef2ba` |
| Freeze Security and ML preferences | `0x0d0f54af39c3eebe611d93d73f66a962ec3eb780c284ecc09854f5cbeaf3bbb1`; `0x65ccc35c6cab213005a0f69dbc8566e3454fa729b24f40fc95ff6c7ed11dddab` |
| Seal Security, ML, market 1 | `0xec900e369d360d4fe185127f04b44585a41cf2a0429be1cd97874e7d996cf78d`; `0xec5868a846453086256a00d04f77e6d091ac3a4c82d272b7c7358a4863c0d7fb`; `0x2a2ba81ac2bc464f2d00f9b8571d5aa5d8576dba6b5646cd99a0ab7b63304723` |
| Qualify Alice→Security, Alice→ML, Bob→Security, Bob→ML, Carol→Security, Carol→ML | `0xa79c8fbeaa8c33e35270bd19aa65aa51911b0085db05808956609d4c420c4889`; `0x148817aec7e12598ffe0795cb8f9189f60dbbe6cc9ba84338865322ff7cabbc8`; `0xe92f45e96612a9e97e289dc2a1bfe5225db5422a68d9d5b4533249b30e948286`; `0x63d32d46a91fe68af06ff5e21a49572c761f14dbb9e6cbbe67438c8fad9e4763`; `0x074d1ea66a691af6427144894ae391024c169c81d5745396678119a0ae52e808`; `0xcbfddaf5b33ae1b1c60cb29a039e4af8fbe2c59bbd449b5c1a01954f895d2996` |
| Compute matching 1 | `0x8f6ce7c0dbf17abac85758359b2b8865c5a02f58f4982282aa6d70e48c7f55ca` |

All six qualification receipts were `ELIGIBLE`: Alice→Security `3f610b7746fb41dfc47020272beb5c8deb0db606127078845e567ac64a69c240`; Alice→ML `e3e5925f4e1d909416c97daedad4480eb4a66e711bfe1207cfcc214ae817ff11`; Bob→Security `3053aedb15f2f291d6cc7adbde899bd95ab4d6223e93f6282efb9e2c3e6506be`; Bob→ML `826f51662e4a987ee91a4d708e13a6c1ae3a1ed804f118185aa1a8138133d18c`; Carol→Security `c7633a05630b3e86cb11fc0f8dd33bbb359ee64e95d4ba30cb947538576f9ebe`; Carol→ML `050c6cbd5308aa2a50bd89dad295690bb187861e02bc1b75eb18b568eab4c1ea`.

### Fail-closed market 2 on corrected deployment

Market 2 on the corrected contract used candidate 4 and opportunity 3 with mutually listed preferences and a commit-pinned path to a nonexistent raw fixture. Qualification call `0x0c126fac9390d113b9182cc94ef8bb2683d1dafa945513da7c35543bc28e286e` returned `UNAVAILABLE` (status 4), empty evidence, reason `all candidate evidence sources were unavailable`, pair hash `0f952b228c600c392b817ef96f9754407bab0518032c19bbacec9dc5eb8480bc`. The matching attempt `0xdff048c5f2188777fa2a0b3f85108272d09b33df4b98e82847c272c243137f94` reached receipt status `FINALIZED`, but wrote no matching state: readback remained `SEALED`, matching hash empty, proposal count 0. This is the expected fail-closed result because `UNAVAILABLE` is retryable and cannot be used to seal an incomplete eligible graph. Market 2 setup transactions were create `0x940b779bc94e34127b4fba57d642d9f4606616a633b6d0aef29ec1bfa29672af`, register opportunity `0x17863e7d01e6434b0e36f74b9bcfaad5f10992435fceb9e15df1f64d0302ba6d`, register candidate `0x55ebd500e80924e7468e08246777ce1dce18af6d5ee7d940572f17e3485e36da`, add unavailable source `0xb8933d927083fc16861f9130235f075d6b524d6e42765d468f72c1febcf2d8dd`, set candidate and opportunity preferences `0x42a00dd4443d4d2f3a6e0b01b6ee53fde5fce81614aa14593cf2527b826dd61` and `0xc52493bd9152a5896990b1c3d1d5c25d82e09ed32db4289a6c6e45770f1f928c`, seal candidate/opportunity/market `0x8984bbc7fc87d1b8daecb274c69c8ecee449d78fdf79fb8d3040b183756e4140`, `0xc76ed8270472c3e0aa4538191de064eaac25b2c81e7da6fe1594319ac2997866`, `0x59671121d8c899a6bb48d66b5a2d7579ddcb5d0a59024cddace1538f09309d2d`. An earlier malformed qualification probe `0xb50519b5db7d6139985650c9fd1b57fc23b11b5817a6b57cccdb47ed17efffd3` used three arguments for a two-argument method and produced no state change; the two-argument retry above is the recorded qualification result.

### NOT_ESTABLISHED graph-exclusion market 3 on corrected deployment

Market 3 used candidate 5 / opportunity 4 with a commit-pinned Bob fixture and the requirement for public evidence of a current active medical license. Qualification transaction `0x2ba35816db63218770bfee2a8ad255c192d68b39f605bae8067a4b7f7b66bd3a` returned `NOT_ESTABLISHED` (status 2), empty evidence, reason `No public evidence provided of a current active medical license as required`, and pair hash `d1049aa9d484ef642b29f9eb1ef0c0415f111dd29ee0b77d715b065bc40c187c`. Market 3 definition hash: `b9a9c2567d67c17b4430f866f854739e407f764b9660ae1dbb2acc2bbec3f0d5`. Matching transaction `0x3f19393958176ffcac651af21702cbc7501d4a96159f0759017c8caebb5aed58` produced matching hash `788de71b58810c89854a1fe5f11e028121f421ccf6e93423f21479d3faef8f45`, proposal count 1, candidate 5 unmatched (`get_match(5) == 0`), and `blocking_pair_count(3) == 0`.

Market 3 setup transactions: create `0x9c9e5de58ce77c2904869c2be99848bdf5db468239d2588eb8e29f5bd10223b0`; register opportunity 4 `0x55b74666288aeaa8e1dda5c5d0c876de337eec954bb528d7eedd197e5b459749`; register candidate 5 `0x1423a9ed7744c689c817fd39064719de3596e8e5fb2ea031fb0d45cae5bda1ce`; add Bob pinned source `0x50db1fbe890ddb0f832213d4c4789d2dd750558cce797d5fbe5a44f09ab2d8a0`; set candidate and opportunity preferences `0xc2076f239338c7f1538a8bd76cb476053f1cac593d133801726864d2536ff12b` and `0xf8a5b2e2378a6ac8dc9d55c16b5842b375febd6f5c52415ae05f4914d164320c`; seal candidate, opportunity, and market `0x56bc9ab3eb9085bf2ba24710562154f7e7eeb0fe745c2dade9e83ffa1ec52e71`, `0x6e205c9ba6282fee21bcecd811735b4884a899b98a828befc670af5405e5e623`, `0x4f350ec29bc6bf15ee9fedfe0ea9ad1c507659210a6f33a9d136386d62b6a129`.

## Historical deployment evidence

The following deployment and lifecycle evidence records the earlier source, before registration admission was added. It is retained for audit history and is superseded for the current contract identity by the corrected deployment and live proof above.

### Historical deployment identity (superseded)

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

### Historical local verification

- Unit/property suite: **12 passed**.
- Direct Mode suite: **32 passed**, pinned stable GenVM `v0.2.16`.
- GenVM lint: **3 checks passed**.
- GenVM SDK semantic validation: **passed**, StableMatch with 21 methods (9 views, 12 writes).
- Python compileall: **passed**.
- Repository preflight: **passed**, UTF-8 LF-normalized contract SHA-256 `c391f8384ae04101f48af1c9d23b2dcea932dc85788c585e2c15acb27a7490d2`.
- Repository-local CLI: `genlayer@0.39.1`.

### Historical flagship market 1

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

### Historical fail-closed market 2

Market 2 used a mutually listed candidate 4 / opportunity 3 pair and a commit-pinned raw GitHub path for a nonexistent fixture. Qualification transaction `0xbea9c771176e8abaeebb351a1cbe7cca48eeb58b86a33b114a61579bcc538d56` produced `UNAVAILABLE` (status 4), empty evidence, pair hash `cb564bebe47b4fd0eb9de25a092eb66c79f18693367ef9c4abd2530af876d832`. The `compute_matching(2)` attempt `0x0e6ad273405f65a77b34a8b134602b2e7f9ebfedb1f694652298e7a8e2082cfd` finalized with leader execution result `ERROR`; readback remained `SEALED`, matching hash empty, candidate 4 unmatched. No matching state was written.

Market 2 setup transactions: create `0xc38733046ab79a73ea7b201cdf07a6bc4e31e462d60280651b4da8bbed4ec825`; register opportunity 3 `0xff265a7044267f956e308129fa5c1163193ba4459091ff7f10a827faae81687a`; register candidate 4 `0x8e37df96f8d7a8fee4e5336572de066562268133471d7678bc73c26ea045521f`; add unavailable source `0x0dc7fae38e5964beccc448ca996bbe97c5d4dbf308073c915597559574bba573`; candidate preferences `0xad27af8edd2cd59968f7474044c2a37854b6f526acd190ad46db06c118e2703a`; opportunity preferences `0xa1352d807e55ff0942c9601db3b98f37e86460801730d24db26ca183d7c14aa7`; seal candidate `0x01db51c85804790d62347dcc527180c9dfddb780e9335f23e40b4d4c575d727f`; seal opportunity `0x9bb7ace7b9290d91c1b4e259779076e5a8d945f8e551b1b9efd2e44d98d0e631`; seal market `0xbaa94df06540202b400782bdcf189a68193c731107a1c2877d084673d9b0dad0`.

### Historical NOT_ESTABLISHED graph-exclusion market 3

Market 3 definition hash: `0e011eddcf5fd0c1d8c7652646516790b40228db4451c13123b97e48e1ab666e`. Candidate 5 / opportunity 4 were mutually listed; the pinned Bob fixture did not establish the law-degree requirement. Qualification transaction `0xd3f94ef9e40db15bb81e43520698821485790ab1ddab5eab3d283e7ee694f801` produced `NOT_ESTABLISHED` (status 2), empty evidence, pair hash `6c66c1d7a16c51f1f6ae608b66cd4b52757041c788f274f532761fedd842c479`. Matching transaction `0x31143e163ccf49ab52502cf8053c67c895a5867fde220241be310fd25426c2a6` finalized the market with candidate 5 unmatched, matching hash `655222315edb50fd2b08d7a9a8109e50551dc007c20479d45878c7b62dbdb37d`, and blocking-pair count **0**.

Market 3 setup transactions: create `0x3716db560cdee9d254271fe2940f36fe67c81306500e40b5f95ccccd9e10de75`; register opportunity 4 `0xa468a2c4d264f1d00e9f69fe5b988e8a82e1c1ea045e7e07e775275a666c059a`; register candidate 5 `0xd60b1d8f3bbcf336f87dc819609feb65d7d4262c6a471b8597bc45f620ae8d4f`; add pinned source `0x4f7eaa5160dc47628f169985e16939983a238ea2fd70d0b3d5ce32cf2316be36`; candidate preferences `0x189b39d123f3af747bbd0f25f9965327bcae24f23e96a1ac4b77b612bc89d002`; opportunity preferences `0xc3880f8d454389601518af84e95acd4bfbccce8f7d6d8052b5c7bdef5ee6486e`; seal candidate `0x22b30f2b0871fbe42a879df14191c4ef993d8ddbc5ebde6a566051db6595c58d`; seal opportunity `0xe2ac47ed17ca299af1d7b44ec337ebef0b6bb794059e682faf3e45dcaa7dbc93`; seal market `0x65a22480a85ea64372a91a9f3ce3a2f74efa3f74c7eb66449da57de341855dbc`.

### Scope and limitations of historical evidence

This is a Studionet demonstration, not identity proof or a permanent credential. The evidence sources are public demo fixtures. The deployed contract is byte-for-byte the committed contract; the LLM determined eligibility classes only, while the frozen participant rankings and deterministic matching code produced the assignments. The documented DNS rebinding and redirect-egress limitation remains part of the evidence-renderer trust boundary.
