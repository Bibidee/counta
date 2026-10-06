# Counta deployment and release evidence

## Current deployed release: v0.3.3

| Evidence | Verified value |
|---|---|
| Network | GenLayer Studionet, chain ID 61999 |
| Frozen source commit | `7fa406e9f5d712c237d241c6a5daedf04b2b5909` |
| Release tag | `v0.3.3` (annotated tag at frozen source commit) |
| Contract SHA-256 | `c1160498a29145ac2806a555ec5121d5e858a16d384ec5184b11f9cb68272ff6` |
| Git blob SHA | `85646a19c6171e6503b47151b902917c0b7cf4b1` |
| Source size | 38,570 bytes locally and as retrieved from Studionet |
| Contract address | [`0xC3402F827Ba8E6ee706A8290B4a47d2b447285B2`](https://explorer-studio.genlayer.com/address/0xC3402F827Ba8E6ee706A8290B4a47d2b447285B2) |
| Deployment transaction | [`0x5627121e05f5e0ccfed6071b978049dd2b215023dafbbef91894fce1ed5b15a7`](https://explorer-studio.genlayer.com/tx/0x5627121e05f5e0ccfed6071b978049dd2b215023dafbbef91894fce1ed5b15a7) |
| Deployment result | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS |
| Source parity | VERIFIED byte-for-byte using official GenLayer CLI source retrieval; 38,570 bytes and SHA-256 match |
| Frozen-source GitHub Actions | [run 37456630767](https://github.com/Bibidee/counta/actions/runs/37456630767): completed, success, exact source commit |
| Frozen-source release gate | 132 passed, 0 failed, 0 skipped; preflight, GenVM lint and ABI/schema passed |
| `get_info()` | `name=Counta`, `version=0.3.3`, `min_confidence=75`, `max_text_artifact_bytes=16000`, `max_image_artifact_bytes=2000000`, `semantic_attempt_telemetry_cap=1000`, `infrastructure_attempt_telemetry_cap=3`, `review_retry_cooldown_seconds=900`, `review_cooldown_model=party_specific`, `min_deposit=1000000000000000`, `milestone_capacity=unbounded_by_contract`, `identity_model=sponsor_scoped_composite_reference`, `evidence_authority_model=sponsor_fixed_exact_hostname`, `infrastructure_failure_policy=retry_after_cooldown_until_review_deadline`, `evidence_failure_policy=retry_until_deadline` |

The v0.3.3 deployment is the current submission candidate. The v0.3.2 and
earlier deployments below are historical and superseded; their addresses,
receipts, and tests are retained as historical evidence only.

### v0.3.3 live approved beneficiary payout

Milestone ID: `COUNTAV33-APPROVE-20261006`. Canonical reference:
`0x7c65ce913f5665c11f1219048112c84cd6cb2a4b:COUNTAV33-APPROVE-20261006`.
Sponsor: `0x7C65cE913F5665c11f1219048112C84CD6cb2a4B`. Designated beneficiary:
`0x2cd419603eBa593074653930Ddc4073d4FD8fc60`. Deposit: 0.001 GEN
(`1000000000000000` wei).

Deliverable URL:
[`https://cdn.jsdelivr.net/gh/Bibidee/counta@071996036e902ed184d8c06a49aec7896b0f06aa/evidence/live-v033-approved-deliverable.txt`](https://cdn.jsdelivr.net/gh/Bibidee/counta@071996036e902ed184d8c06a49aec7896b0f06aa/evidence/live-v033-approved-deliverable.txt),
214 raw bytes, SHA-256
`f47a425d02fc1192f3367bc2b8a7ddd52b53d49f6525ced580d37903e118f5e2`.
Evidence URL:
[`https://raw.githubusercontent.com/Bibidee/counta/071996036e902ed184d8c06a49aec7896b0f06aa/evidence/live-v033-approved-evidence.txt`](https://raw.githubusercontent.com/Bibidee/counta/071996036e902ed184d8c06a49aec7896b0f06aa/evidence/live-v033-approved-evidence.txt),
370 raw bytes, SHA-256
`ef4f035f0ee08ffa7a726d56004d9685d557cf1b8228e8a1a18c10ad5fb0e54b`.
Both fixtures are repository-owned; they demonstrate committed-byte and
protocol behavior, not independent authorship or real-world truth.

| Step | Transaction | Finalized result |
|---|---|---|
| `create_milestone` | [`0xa6139436a45eda11ec46fb7e54503837076acb4a8a41084589abde67cf3b8554`](https://explorer-studio.genlayer.com/tx/0xa6139436a45eda11ec46fb7e54503837076acb4a8a41084589abde67cf3b8554) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; 0.001 GEN credited |
| `accept_milestone` | [`0xa355ea4e23f0f5273e673aaebede9e0d7159deefc750af1616362b540e718a7c`](https://explorer-studio.genlayer.com/tx/0xa355ea4e23f0f5273e673aaebede9e0d7159deefc750af1616362b540e718a7c) | FINALIZED / MAJORITY_AGREE; canonical milestone active |
| `submit_delivery` | [`0x4ac82a845d10e058ea83b5463919dca97fe0bbf9df70dcb4ebd7856bdb749049`](https://explorer-studio.genlayer.com/tx/0x4ac82a845d10e058ea83b5463919dca97fe0bbf9df70dcb4ebd7856bdb749049) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; committed URLs and hashes stored |
| `review` | [`0xa355792181e95fc7462f24ed4b68e0d36e389e82675daf814c8b44897bd3455c`](https://explorer-studio.genlayer.com/tx/0xa355792181e95fc7462f24ed4b68e0d36e389e82675daf814c8b44897bd3455c) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; approved, confidence 82 |
| `settle` | [`0x4cccdb1f11996c75c4e2816d69648246ade66d44b511184d9632294d3f960e21`](https://explorer-studio.genlayer.com/tx/0x4cccdb1f11996c75c4e2816d69648246ade66d44b511184d9632294d3f960e21) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; beneficiary transfer dispatched |
| Child transfer | [`0x40a3cfe7d53bac5b3bd2ce1989b6ce9729fce4f5ba51a58d06952799142d2592`](https://explorer-studio.genlayer.com/tx/0x40a3cfe7d53bac5b3bd2ce1989b6ce9729fce4f5ba51a58d06952799142d2592) | FINALIZED; 1,000,000,000,000,000 wei to beneficiary; `value_credited=true`; child result `NO_MAJORITY` |

The final canonical read reported `payout_dispatched`, `deposited=0`,
`beneficiary_dispatched_amount=1000000000000000`, and
`sponsor_dispatched_amount=0`. The child receipt independently confirms the
beneficiary credit. The stored review rationale was: “The committed text
deliverable accurately states both required features: separate
sponsor/beneficiary cooldowns and retryable evidence retrieval failures until
the fixed deadline. The evidence corroborates both claims referencing separate
next_review_at fields and evidence_unavailable mapping. No contradictions or
missing conditions detected.”

### v0.3.3 live semantic rejection and sponsor refund

Milestone ID: `COUNTAV33-BLOCKED-20261006`; deposit 0.001 GEN. The deliverable
claimed that every settlement goes to the sponsor, while the evidence stated
that approved milestones pay the beneficiary. This is a genuine contradictory
semantic case.

Deliverable URL:
[`https://cdn.jsdelivr.net/gh/Bibidee/counta@071996036e902ed184d8c06a49aec7896b0f06aa/evidence/live-v033-blocked-deliverable.txt`](https://cdn.jsdelivr.net/gh/Bibidee/counta@071996036e902ed184d8c06a49aec7896b0f06aa/evidence/live-v033-blocked-deliverable.txt),
96 raw bytes, SHA-256
`80d80e7feb5ad78213609acb181d2e6fa8248f3b43ab34022585c73e8d060396`.
Evidence URL:
[`https://raw.githubusercontent.com/Bibidee/counta/071996036e902ed184d8c06a49aec7896b0f06aa/evidence/live-v033-blocked-evidence.txt`](https://raw.githubusercontent.com/Bibidee/counta/071996036e902ed184d8c06a49aec7896b0f06aa/evidence/live-v033-blocked-evidence.txt),
264 raw bytes, SHA-256
`ec8594bb70d7991f3f5cb4719814ac7f1b28d11e48a2ff4dad01acfd4230aed8`.

| Step | Transaction | Finalized result |
|---|---|---|
| `create_milestone` | [`0x7998c81354ce698853b96faf716a6a89f32975a15bf4f71d3ba49efee932569c`](https://explorer-studio.genlayer.com/tx/0x7998c81354ce698853b96faf716a6a89f32975a15bf4f71d3ba49efee932569c) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; 0.001 GEN credited |
| `accept_milestone` | [`0x9c842437e7c70c0931f01fafab1350c70a4d129d5054b44ec59409d1aaaa8e13`](https://explorer-studio.genlayer.com/tx/0x9c842437e7c70c0931f01fafab1350c70a4d129d5054b44ec59409d1aaaa8e13) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS |
| `submit_delivery` | [`0x2f92500b990bd59e0c70801fafab1350c70a4d129d5054b44ec59409d1aaaa8e13`](https://explorer-studio.genlayer.com/tx/0x2f92500b990bd59e0c70801fafab1350c70a4d129d5054b44ec59409d1aaaa8e13) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; committed URLs and hashes stored |
| `review` | [`0x83886f01515764166c1b22a89024a15978f2295775b7245878319d12cb3035a9`](https://explorer-studio.genlayer.com/tx/0x83886f01515764166c1b22a89024a15978f2295775b7245878319d12cb3035a9) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; blocked, confidence 100, `semantic_rejection` |
| `settle` | [`0x548e70e93736fbca5ba3c15dc40d5c22dbc79120d48a19cd8bfdaded49a7f802`](https://explorer-studio.genlayer.com/tx/0x548e70e93736fbca5ba3c15dc40d5c22dbc79120d48a19cd8bfdaded49a7f802) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; sponsor refund dispatched |
| Child transfer | [`0xe5a98c11bf8b21d12633a47937dc9ad1a0e2b8f2fff0e1beff02ddb2de8ae422`](https://explorer-studio.genlayer.com/tx/0xe5a98c11bf8b21d12633a47937dc9ad1a0e2b8f2fff0e1beff02ddb2de8ae422) | FINALIZED; 1,000,000,000,000,000 wei to sponsor; `value_credited=true`; child result `NO_MAJORITY` |

Canonical final state: `refund_dispatched`, `deposited=0`,
`sponsor_dispatched_amount=1000000000000000`, and
`beneficiary_dispatched_amount=0`. The child receipt confirms sponsor credit.

### v0.3.3 live evidence recovery and party-specific cooldown

Milestone ID: `COUNTAV33-RECOVERY-20261006`; deposit 0.001 GEN. The committed
evidence URL initially returned a real HTTP 404. Its exact repository-owned
bytes were later published at that same URL and then verified successfully.
This mutable `main` URL was used specifically to exercise availability
recovery; it is not a recommendation for production evidence commitments.

Deliverable URL:
[`https://cdn.jsdelivr.net/gh/Bibidee/counta@071996036e902ed184d8c06a49aec7896b0f06aa/evidence/live-v033-recovery-deliverable.txt`](https://cdn.jsdelivr.net/gh/Bibidee/counta@071996036e902ed184d8c06a49aec7896b0f06aa/evidence/live-v033-recovery-deliverable.txt).
Evidence URL:
[`https://raw.githubusercontent.com/Bibidee/counta/main/evidence/live-v033-recovery-evidence.txt`](https://raw.githubusercontent.com/Bibidee/counta/main/evidence/live-v033-recovery-evidence.txt),
SHA-256 `23b6b651af6d082dfaa4c153620a56c8a8ad85140b60e44b925f71b53cfbe151`,
249 bytes.

| Step | Transaction | Finalized result |
|---|---|---|
| `create_milestone` | [`0xabedee8e4a1b1ee7af3eb72e1b09e18f070c8fa7c7139093f6eefb0ec6531415`](https://explorer-studio.genlayer.com/tx/0xabedee8e4a1b1ee7af3eb72e1b09e18f070c8fa7c7139093f6eefb0ec6531415) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS |
| `accept_milestone` | [`0x42b25f0391eba36fca0df0433d9aecd2e6fa2a6d96ad0f743bde7ea07ff09622`](https://explorer-studio.genlayer.com/tx/0x42b25f0391eba36fca0df0433d9aecd2e6fa2a6d96ad0f743bde7ea07ff09622) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS |
| `submit_delivery` | [`0x37fe05494102bb93a24ff3db844c2cb71f741383235639821bcb1d1f924e0575`](https://explorer-studio.genlayer.com/tx/0x37fe05494102bb93a24ff3db844c2cb71f741383235639821bcb1d1f924e0575) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS |
| Initial review | [`0x4bea2f2787e5dd3583c1bf7efb2cb39c116b30d3e6ac93591b670e3e80659206`](https://explorer-studio.genlayer.com/tx/0x4bea2f2787e5dd3583c1bf7efb2cb39c116b30d3e6ac93591b670e3e80659206) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; `retryable`, `evidence_unavailable`; infrastructure attempts 1, semantic attempts 0, deposit retained |
| Beneficiary retry review | [`0x2cdb14790ea7e05fe4ca7c7cebf943cff46fbe4bf0306bf999924d7053e27ad2`](https://explorer-studio.genlayer.com/tx/0x2cdb14790ea7e05fe4ca7c7cebf943cff46fbe4bf0306bf999924d7053e27ad2) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS while sponsor cooldown was active; approved, confidence 95 |
| `settle` | [`0xe2329e309e99e3cac95d7fda55c7b67e2d9ea0ac3434f7e97684060ab993b566`](https://explorer-studio.genlayer.com/tx/0xe2329e309e99e3cac95d7fda55c7b67e2d9ea0ac3434f7e97684060ab993b566) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; beneficiary transfer dispatched |
| Child transfer | [`0xc610ab83004d598ccc877b6779ee1a906fc3e94eab3a51a58d06952799142d2592`](https://explorer-studio.genlayer.com/tx/0xc610ab83004d598ccc877b6779ee1a906fc3e94eab3a51a58d06952799142d2592) | FINALIZED; 1,000,000,000,000,000 wei to beneficiary; `value_credited=true`; child result `NO_MAJORITY` |

The first retryable review set only the sponsor's cooldown to
`1791288721`; `beneficiary_next_review_at` remained `0`. The beneficiary's
review succeeded without waiting for that sponsor cooldown, and final
settlement returned the full deposit to the beneficiary. The rationale stated
that the deliverable matched the brief and the evidence supported the exact
deliverable. The final canonical read showed `payout_dispatched` and
`deposited=0`.

The release gate on the frozen source commit passed 132 tests; exact-source
CI run [37456630767](https://github.com/Bibidee/counta/actions/runs/37456630767)
passed. Final documentation-head CI will be recorded after the evidence update
and all local gates complete.

## Historical deployed release: v0.3.2 (superseded)

| Evidence | Verified value |
|---|---|
| Network | GenLayer Studionet, chain ID 61999 |
| Frozen source commit | `e546d8b83c67adb67fd0780961e1159822b14980` |
| Release tag | `v0.3.2` |
| Contract SHA-256 | `ae899a586ee77a316870a800aa8c4baf9c12d7f8267320d14691327dc551f1ac` |
| Git blob SHA | `4946d1481f93f3e8fb93710f50167e3d034e2b7e` |
| Source size | 36,598 bytes locally and as retrieved from Studionet |
| Contract address | [`0x5E7D5C3039713b50aD46d09C3c1ad0c7194ce07e`](https://explorer-studio.genlayer.com/address/0x5E7D5C3039713b50aD46d09C3c1ad0c7194ce07e) |
| Deployment transaction | [`0xca44755d4d4166f238d3a5243e66c721d5870c3f2180b294a21b42d905fe0c12`](https://explorer-studio.genlayer.com/tx/0xca44755d4d4166f238d3a5243e66c721d5870c3f2180b294a21b42d905fe0c12) |
| Deployment result | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS |
| Source parity | VERIFIED byte-for-byte: official GenLayer CLI code retrieval was decoded and compared with frozen local source; both are 36,598 bytes and have the same SHA-256 |
| Frozen-source GitHub Actions | [run 37430349521](https://github.com/Bibidee/counta/actions/runs/37430349521): completed, success, exact source commit |
| Fixture-commit GitHub Actions | [run 37432617416](https://github.com/Bibidee/counta/actions/runs/37432617416): completed, success, exact fixture commit |
| Frozen-source release gate | 105 passed, 0 failed, 0 skipped; preflight, GenVM lint and ABI/schema passed |
| `get_info()` | `name=Counta`, `version=0.3.2`, `min_confidence=75`, `min_deposit=1000000000000000`, text/image limits `16000/2000000`, review cooldown `900`, semantic telemetry cap `1000`, infrastructure telemetry cap `3`, evidence authority `sponsor_fixed_exact_hostname`, identity `sponsor_scoped_composite_reference`, infrastructure policy `retry_after_cooldown_until_review_deadline`, milestone capacity `unbounded_by_contract` |

The v0.3.2 deployment and the live evidence below are historical and
superseded by v0.3.3. The v0.3.1 deployment evidence is also retained as
historical evidence only.

### v0.3.2 live approval and beneficiary payout

Milestone ID: `COUNTA-V032-APPROVED-20261006-001`. Canonical reference:
`0x7c65ce913f5665c11f1219048112c84cd6cb2a4b:COUNTA-V032-APPROVED-20261006-001`.
Sponsor: `0x7C65cE913F5665c11f1219048112C84CD6cb2a4B`. Designated beneficiary:
`0x2cd419603eBa593074653930Ddc4073d4FD8fc60`. Deposit: 0.001 GEN
(`1000000000000000` wei). The brief requested a verification of the frozen
v0.3.2 source, SHA-256, release test result, and exact-head CI record.

Deliverable URL:
[`https://raw.githubusercontent.com/Bibidee/counta/b577f4dcdbcd6d109905bf1554c4aebfc1883e86/evidence/live-v032-release-attestation.txt`](https://raw.githubusercontent.com/Bibidee/counta/b577f4dcdbcd6d109905bf1554c4aebfc1883e86/evidence/live-v032-release-attestation.txt),
424 raw bytes, SHA-256
`1425cbd893959607fe6f4186941231d92b8e83f787428228a3606cfaf80de8a0`.

Evidence URL:
[`https://api.github.com/repos/Bibidee/counta/actions/runs/37430349521`](https://api.github.com/repos/Bibidee/counta/actions/runs/37430349521),
11,529 raw bytes, SHA-256
`b126f397dd286e5dd87ff6445ef66832ba4ad700e8af83133daebc77dbc08fff`.
The API record confirmed GitHub Actions success and the matching source
`head_sha`; it is GitHub-generated evidence, not independent human-authored
corroboration. The deliverable fixture is repository-owned.

| Step | Transaction | Finalized result |
|---|---|---|
| `create_milestone` | [`0xba3de3203231ddc6b7c892f549cbc0344d1fa2b177b9367f803e7293b1154a8c`](https://explorer-studio.genlayer.com/tx/0xba3de3203231ddc6b7c892f549cbc0344d1fa2b177b9367f803e7293b1154a8c) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; 0.001 GEN credited |
| `accept_milestone` | [`0x744437aacba3ba6b6475d436f5ecd10d3523b042ae4bf35af026d1cd59a4c323`](https://explorer-studio.genlayer.com/tx/0x744437aacba3ba6b6475d436f5ecd10d3523b042ae4bf35af026d1cd59a4c323) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS |
| `submit_delivery` | [`0xf3f67d60e205777264571cabdac56d830da9e2e1e02476cd025b2c0479265037`](https://explorer-studio.genlayer.com/tx/0xf3f67d60e205777264571cabdac56d830da9e2e1e02476cd025b2c0479265037) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; committed URLs and hashes stored |
| `review` | [`0x3d89d2e02d4d23ecb0c618d7718ec4eb8c8dbf63ea995db05ece205959574412`](https://explorer-studio.genlayer.com/tx/0x3d89d2e02d4d23ecb0c618d7718ec4eb8c8dbf63ea995db05ece205959574412) | FINALIZED / MAJORITY_AGREE; leader GenVM SUCCESS; approved, confidence 100 |
| `settle` | [`0xbafb58bddfe8024c03c46738af9d30093035a6d312c20657ddc3eb38a970c4e3`](https://explorer-studio.genlayer.com/tx/0xbafb58bddfe8024c03c46738af9d30093035a6d312c20657ddc3eb38a970c4e3) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; beneficiary transfer dispatched |
| Child transfer | [`0x72ea6432d7d844879d1e12e31ba4b8678903f6bf891c435a21c6f9541ad199b3`](https://explorer-studio.genlayer.com/tx/0x72ea6432d7d844879d1e12e31ba4b8678903f6bf891c435a21c6f9541ad199b3) | FINALIZED; Counta sender to beneficiary; `1000000000000000` wei; `value_credited=true`; child result `NO_MAJORITY` |

The canonical final read reports `payout_dispatched`,
`settlement=beneficiary_payout_dispatched`, `deposited=0`,
`dispatched_amount=1000000000000000`,
`beneficiary_dispatched_amount=1000000000000000`, and
`sponsor_dispatched_amount=0`. The separate child receipt confirms the
beneficiary credit. The stored review rationale was: “The deliverable matches
all requirements in the brief: frozen source commit (e546d8b8...), SHA-256
(ae899a58...), 105 tests passed, and successful lint/schema/preflight. The
supporting evidence (GitHub API response) confirms that run 37430349521
completed with 'success' on the exact head_sha
e546d8b83c67adb67fd0780961e1159822b14980.” The beneficiary balance increased
by exactly 0.001 GEN between the recorded before/after reads.

### v0.3.2 live explicit rejection and sponsor refund

Milestone ID: `COUNTA-V032-BLOCKED-20261006-001`. Canonical reference:
`0x7c65ce913f5665c11f1219048112c84cd6cb2a4b:COUNTA-V032-BLOCKED-20261006-001`.
The sponsor and beneficiary were the same addresses as above; deposit was
0.001 GEN. The brief required the deliverable's first line to be exactly
`MILESTONE COMPLETE` and to state completion. The committed deliverable
explicitly stated that work was not complete.

Deliverable URL:
[`https://raw.githubusercontent.com/Bibidee/counta/b577f4dcdbcd6d109905bf1554c4aebfc1883e86/evidence/live-v032-incomplete-deliverable.txt`](https://raw.githubusercontent.com/Bibidee/counta/b577f4dcdbcd6d109905bf1554c4aebfc1883e86/evidence/live-v032-incomplete-deliverable.txt),
119 raw bytes, SHA-256
`5e4b635c1b890c55a56be5c107c83c7aeb0bb9d8fb63465cd54e290018b4c879`.

Evidence URL:
[`https://cdn.jsdelivr.net/gh/Bibidee/counta@b577f4dcdbcd6d109905bf1554c4aebfc1883e86/evidence/live-v032-incomplete-verification.txt`](https://cdn.jsdelivr.net/gh/Bibidee/counta@b577f4dcdbcd6d109905bf1554c4aebfc1883e86/evidence/live-v032-incomplete-verification.txt),
137 raw bytes, SHA-256
`ac2ed1fa16fabba26f2d695e947d91409c887241a580d6684ac3c69de9ebf286`.
Both fixtures are repository-owned, not independent human-authored sources.

| Step | Transaction | Finalized result |
|---|---|---|
| `create_milestone` | [`0xf7e671ce29164f5538e3046989615b46f8b337ebe5f0940f5245bab8a18de519`](https://explorer-studio.genlayer.com/tx/0xf7e671ce29164f5538e3046989615b46f8b337ebe5f0940f5245bab8a18de519) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; 0.001 GEN credited |
| `accept_milestone` | [`0xb7b0baa7db010066a9f349742ee5655d7fa83583188c5273ecce29b8d8d4f30f`](https://explorer-studio.genlayer.com/tx/0xb7b0baa7db010066a9f349742ee5655d7fa83583188c5273ecce29b8d8d4f30f) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS |
| `submit_delivery` | [`0x89b2e2faae0f582fd5cc2125025ac0353757b7e67dff8ca4e09bdb67ec217774`](https://explorer-studio.genlayer.com/tx/0x89b2e2faae0f582fd5cc2125025ac0353757b7e67dff8ca4e09bdb67ec217774) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; committed URLs and hashes stored |
| `review` | [`0x29d26942462dcbfaf27fdfd3bab4c287465b06764a0144d9407196d470159052`](https://explorer-studio.genlayer.com/tx/0x29d26942462dcbfaf27fdfd3bab4c287465b06764a0144d9407196d470159052) | FINALIZED / MAJORITY_AGREE; leader GenVM SUCCESS; blocked, confidence 99, reason `semantic_rejection` |
| `settle` | [`0x76b5e36b87e599ba6d9a3fa71727aa31bd4790385697f68731f8425319882a9e`](https://explorer-studio.genlayer.com/tx/0x76b5e36b87e599ba6d9a3fa71727aa31bd4790385697f68731f8425319882a9e) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; sponsor refund dispatched |
| Child transfer | [`0x13116022b0fa609a37b7bdfb3cdac16fdbea85af26685dcd7d435ab9471d0019`](https://explorer-studio.genlayer.com/tx/0x13116022b0fa609a37b7bdfb3cdac16fdbea85af26685dcd7d435ab9471d0019) | FINALIZED; Counta sender to sponsor; `1000000000000000` wei; `value_credited=true`; child result `NO_MAJORITY` |

The final canonical read reports `refund_dispatched`,
`settlement=sponsor_refund_dispatched`, `deposited=0`,
`dispatched_amount=1000000000000000`,
`sponsor_dispatched_amount=1000000000000000`, and
`beneficiary_dispatched_amount=0`. The child receipt confirms the sponsor
credit. The stored rationale identified the deliverable's first line as
`MILESTONE NOT COMPLETE`, noted its explicit statement that no work product
was submitted, and explained the contradiction with the brief. This is an
actual semantic rejection, not a fabricated model result.

### v0.3.2 live paths not claimed

No live 403-to-recovery path or controllable semantic-uncertainty fairness
sequence is claimed; producing those outcomes from a real provider would not
be deterministic, and no controlled genuine 403-to-200 endpoint was used.
No live review-deadline expiry was attempted because the configured window is
three days. The exact behaviors are covered by Direct Mode regression tests;
the live flows above establish approved payout and explicit semantic
rejection/refund only.

## Historical deployed release: v0.3.1 (superseded)

| Evidence | Verified value |
|---|---|
| Network | GenLayer Studionet, chain ID 61999 |
| Frozen source commit | `8c7d472522e90b481bce56794c175e2e951c99fa` |
| Contract SHA-256 | `9b98e0016a38e7c4ad8e613370b0667e7c4b37910e4dbaf26e99a6a1688be005` |
| Git blob SHA | `cc7c60a666d49d5d1293c71967aabdcaaeb95522` |
| Source size | 36,535 bytes locally and as retrieved from Studionet |
| Contract address | [`0xE4Bb7FC4C217EE867F14d40aFaa1e868693CDcAB`](https://explorer-studio.genlayer.com/address/0xE4Bb7FC4C217EE867F14d40aFaa1e868693CDcAB) |
| Deployment transaction | [`0xa8b3ed6c3e0a6b297d5017350c7cef3b46f05fb0b3eb9ae8343a10b7d31ddced`](https://explorer-studio.genlayer.com/tx/0xa8b3ed6c3e0a6b297d5017350c7cef3b46f05fb0b3eb9ae8343a10b7d31ddced) |
| Deployment result | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS |
| Source parity | VERIFIED byte-for-byte using `gen_getContractCode`; local and retrieved source SHA-256 and byte lengths match |
| `get_info()` | Counta 0.3.1; minimum confidence 75; max text artifact 16,000 bytes; max image artifact 2,000,000 bytes; max review attempts 3; infrastructure telemetry cap 3; retry cooldown 900 seconds; minimum deposit `1000000000000000` wei; sponsor-scoped composite identity; sponsor-fixed exact evidence hostname; retryable infrastructure failures can be retried after cooldown until review deadline |
| GitHub CI | PASS on frozen contract commit; run `37351550988` |

The v0.3.1 release changes the v0.3.0 infrastructure retry behavior, rejects
all IP literals and single-label hostnames, and delays beneficiary alias
creation until acceptance. Two v0.3.1 live flows are recorded below: one
semantic rejection that refunded the sponsor, and one release-attestation
approval whose child transfer credited the designated beneficiary. No
v0.3.1 outage/timeout lifecycle is claimed.

### v0.3.1 live milestone flow — blocked and sponsor refund dispatched

The live identifier was `COUNTA-V031-LIVE-20261005-01`. Sponsor:
`0x2cd419603eBa593074653930Ddc4073d4FD8fc60`. Beneficiary:
`0x7C65cE913F5665c11f1219048112C84CD6cb2a4B`. The sponsor deposited the
minimum 0.001 GEN (`1000000000000000` wei); the beneficiary accepted and
submitted the committed artifacts. Both artifact URLs were fetched as raw
bytes before submission, returned HTTP 200, decoded as UTF-8, and matched the
listed SHA-256 values.

Brief: “Complete the committed Counta live demo deliverable and provide
matching evidence.” The short artifacts stated that a demo deliverable was
complete and that verification confirmed it. On-chain semantic review did not
find those assertions substantive enough to demonstrate completed work: it
finalized `blocked`, confidence 18, with rationale that the artifacts asserted
completion but did not visibly demonstrate the live demo or independently
verify the item. This was a semantic rejection, not an infrastructure or hash
failure, and no beneficiary payout was authorized.

Deliverable (59 raw UTF-8 bytes):
[`https://raw.githubusercontent.com/Bibidee/counta/5f1a523ada47aefcc7787f028483f880044c7bd1/evidence/live-deliverable.txt`](https://raw.githubusercontent.com/Bibidee/counta/5f1a523ada47aefcc7787f028483f880044c7bd1/evidence/live-deliverable.txt),
SHA-256 `b2006a039e3ac90264b58902ea6a573fb18f8c4871f0e60af70555287d2eebe9`.

Evidence (82 raw UTF-8 bytes):
[`https://cdn.jsdelivr.net/gh/Bibidee/counta@5f1a523ada47aefcc7787f028483f880044c7bd1/evidence/live-verification.txt`](https://cdn.jsdelivr.net/gh/Bibidee/counta@5f1a523ada47aefcc7787f028483f880044c7bd1/evidence/live-verification.txt),
SHA-256 `48d94b3537b97d678e5d6c436ce686f7837140acfbc7aeadb74caabbb39739a4`.

| Step | Transaction | Finalized result |
|---|---|---|
| `create_milestone` | [`0xae6d2822f1ccdec33d20460f364ad6a7d74b00cd963401ded71598620adb49cc`](https://explorer-studio.genlayer.com/tx/0xae6d2822f1ccdec33d20460f364ad6a7d74b00cd963401ded71598620adb49cc) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; status `funded`; `value_credited=true` |
| `accept_milestone` | [`0xe6fbd27c079f5dc9ab363314ab445e868bd8750d641b3f8c12618316b96cbbab`](https://explorer-studio.genlayer.com/tx/0xe6fbd27c079f5dc9ab363314ab445e868bd8750d641b3f8c12618316b96cbbab) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; status `active` |
| `submit_delivery` | [`0xd00effe34bcc113fd658b0151e72e6d22c1a361c9cb5ba9f953dd9587561b002`](https://explorer-studio.genlayer.com/tx/0xd00effe34bcc113fd658b0151e72e6d22c1a361c9cb5ba9f953dd9587561b002) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; status `submitted`; exact artifact URLs and hashes stored |
| `review` | [`0x3c13a5acf7c17f7744e0b61039fef0fedf350a4cfa235749be9c5031a75dddd4`](https://explorer-studio.genlayer.com/tx/0x3c13a5acf7c17f7744e0b61039fef0fedf350a4cfa235749be9c5031a75dddd4) | FINALIZED / MAJORITY_AGREE / leader GenVM SUCCESS; canonical state `blocked`, confidence 18; one validator voted disagree |
| `settle` | [`0xde71c4f4506a2570eb4291868808fac745dbc2f29353925789b76655916c2986`](https://explorer-studio.genlayer.com/tx/0xde71c4f4506a2570eb4291868808fac745dbc2f29353925789b76655916c2986) | FINALIZED / MAJORITY_AGREE; state `refund_dispatched`; `deposited=0`; sponsor dispatch `1000000000000000` wei |

The canonical post-settlement read confirms the ledger was zeroed and the
full 0.001 GEN refund was dispatched to the sponsor. The child transfer's
recipient-credit flag was not independently recorded here, so this evidence
does not claim `value_credited=true` for the refund. This completes a
fail-closed refund lifecycle, not the approved beneficiary-payment lifecycle.

### v0.3.1 live milestone flow — approved and beneficiary credited

The second live identifier was
`COUNTA-V031-CI-ATTEST-R2-20261005-01`. Sponsor:
`0x2cd419603eBa593074653930Ddc4073d4FD8fc60`. Designated beneficiary:
`0x7C65cE913F5665c11f1219048112C84CD6cb2a4B`. The sponsor deposited the
minimum 0.001 GEN (`1000000000000000` wei); the beneficiary accepted and
submitted one committed deliverable. Its brief requested an exact release-gate
attestation for the frozen v0.3.1 source commit and successful GitHub Actions
run. The semantic reviewer returned `approved`, confidence 100, with rationale
that the deliverable identified the frozen commit and run and the committed
GitHub API evidence confirmed `completed`, `success`, and the matching
`head_sha`.

Deliverable: [`https://raw.githubusercontent.com/Bibidee/counta/d8d814bdb126d91c3f8737bfc4ebbcbf36f45580/evidence/live-v031-release-attestation.txt`](https://raw.githubusercontent.com/Bibidee/counta/d8d814bdb126d91c3f8737bfc4ebbcbf36f45580/evidence/live-v031-release-attestation.txt),
249 raw bytes, SHA-256
`eceddf6026b704c79d2744f5eb4a9b343e24560e37031ba8cedbf785102618f2`.

Evidence: [`https://api.github.com/repos/Bibidee/counta/actions/runs/37351550988`](https://api.github.com/repos/Bibidee/counta/actions/runs/37351550988),
11,529 raw bytes, SHA-256
`7a84ed7289f9d1ffad210d337268fb0ac1e795cd6a28c5aa45440c65c8e42108`.
The checked record identified the same frozen source commit and completed
successfully. This is a GitHub Actions API record, not a second independent
human-authored source.

| Step | Transaction | Finalized result |
|---|---|---|
| `create_milestone` | [`0x278cfa776516cd545d0a61f1c74cd1ae05f0906bf27430339ec86796f7ceff07`](https://explorer-studio.genlayer.com/tx/0x278cfa776516cd545d0a61f1c74cd1ae05f0906bf27430339ec86796f7ceff07) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; funded with 0.001 GEN |
| `accept_milestone` | [`0xe79a932b5122e7039dcb6f41d2a2c4f1600fe3b40ee26980a944804ac8c1b02d`](https://explorer-studio.genlayer.com/tx/0xe79a932b5122e7039dcb6f41d2a2c4f1600fe3b40ee26980a944804ac8c1b02d) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; status `active` |
| `submit_delivery` | [`0x554631f2934b4970b89f61db331d96ba996e95dbd18f331d4ddd56ae563100e4`](https://explorer-studio.genlayer.com/tx/0x554631f2934b4970b89f61db331d96ba996e95dbd18f331d4ddd56ae563100e4) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; status `submitted`; exact URLs and hashes stored |
| `review` | [`0xface3ba3a45512445a7ee6065c450ce68535d38fe3a23df62f0366e97c563659`](https://explorer-studio.genlayer.com/tx/0xface3ba3a45512445a7ee6065c450ce68535d38fe3a23df62f0366e97c563659) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; status `approved`, confidence 100 |
| `settle` | [`0x51fe741fc8af1c0b884652d19f5efabd40e492e1c28cb58362a6e43614c106f7`](https://explorer-studio.genlayer.com/tx/0x51fe741fc8af1c0b884652d19f5efabd40e492e1c28cb58362a6e43614c106f7) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; status `payout_dispatched`, `deposited=0`; beneficiary dispatch `1000000000000000` wei |
| Child transfer | [`0xe4a991e087fdae48922665637cab4ff8e8b537f26d1c59919bb212ea2a15bb66`](https://explorer-studio.genlayer.com/tx/0xe4a991e087fdae48922665637cab4ff8e8b537f26d1c59919bb212ea2a15bb66) | FINALIZED; contract-to-beneficiary transfer of `1000000000000000` wei; `value_credited=true` |

The final canonical `get_milestone()` read returned `status=payout_dispatched`,
`settlement=beneficiary_payout_dispatched`, `deposited=0`,
`beneficiary_dispatched_amount=1000000000000000`, and
`sponsor_dispatched_amount=0`. The separate child receipt confirms the
beneficiary credit. This is the v0.3.1 happy-path proof; it does not erase or
replace the earlier blocked-and-refunded flow.

## Historical deployed release: v0.3.0 (superseded; not v0.3.1)

| Evidence | Verified value |
|---|---|
| Network | GenLayer Studionet, chain ID 61999 |
| Frozen source commit | `5f1a523ada47aefcc7787f028483f880044c7bd1` |
| Contract SHA-256 | `1c3e41f9354ae8dd682d8d7d9e5f4062ac7db8ce647eaca7c3ea27eb9808379e` |
| Git blob SHA | `3b1baab680976c4ed380fb0dca46226a61d7ec59` |
| Source size | 36,339 bytes at the frozen v0.3.0 commit and in deployed code |
| Contract address | [`0x4235915E7ec84596239b2d29B93d1a2A982A1018`](https://explorer-studio.genlayer.com/address/0x4235915E7ec84596239b2d29B93d1a2A982A1018) |
| Deployment transaction | [`0x5ccdb01d7cacf07dfc2ae73b2cbead5e58511c6db338abb486ff4c483c64f5ab`](https://explorer-studio.genlayer.com/tx/0x5ccdb01d7cacf07dfc2ae73b2cbead5e58511c6db338abb486ff4c483c64f5ab) |
| Deployment result | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS |
| Source parity | VERIFIED byte-for-byte via `gen_getContractCode` against the frozen v0.3.0 local source; deployed and frozen-source SHA-256 and lengths equal |
| `get_info()` | Counta 0.3.0; min confidence 75; max text 16,000; max image 2,000,000 bytes; max semantic/infrastructure attempts 3; retry cooldown 900s; minimum deposit `1000000000000000` wei; sponsor-scoped composite identity; sponsor-fixed exact evidence hostname; infrastructure exhaustion expires only at review deadline |
| Frozen-commit release gate | 71 tests passed, 0 skipped, 0 failed; preflight, GenVM lint and ABI/schema passed |
| Frozen-commit GitHub Actions | [run 37342449384](https://github.com/Bibidee/counta/actions/runs/37342449384): completed, success, exact frozen source commit |

The v0.3.0 review liveness limitation was that the shared infrastructure
failure counter stopped all reviews after three outages, even while the review
deadline remained open. Funds were not refundable early, but a party that had
not caused the outage could not obtain a later adjudication after provider
recovery. v0.3.1 removes that lockout; the v0.3.0 behavior remains historical
and is not retroactively changed by the v0.3.1 release.

### v0.3.0 live lifecycle

The live fixture ID was `COUNTA-V030-LIVE-20261005-01`. Sponsor/proposer:
`0x2cd419603eBa593074653930Ddc4073d4FD8fc60`. Beneficiary/consumer:
`0x7c65ce913f5665c11f1219048112c84cd6cb2a4b`. The sponsor deposited the
minimum 0.001 GEN (`1000000000000000` wei). The brief was “Complete the
committed Counta live demo deliverable and provide matching evidence.” The
approved evidence host was `cdn.jsdelivr.net`.

Deliverable (59 raw UTF-8 bytes):
[`https://raw.githubusercontent.com/Bibidee/counta/5f1a523ada47aefcc7787f028483f880044c7bd1/evidence/live-deliverable.txt`](https://raw.githubusercontent.com/Bibidee/counta/5f1a523ada47aefcc7787f028483f880044c7bd1/evidence/live-deliverable.txt),
SHA-256 `b2006a039e3ac90264b58902ea6a573fb18f8c4871f0e60af70555287d2eebe9`.

Evidence (82 raw UTF-8 bytes):
[`https://cdn.jsdelivr.net/gh/Bibidee/counta@5f1a523ada47aefcc7787f028483f880044c7bd1/evidence/live-verification.txt`](https://cdn.jsdelivr.net/gh/Bibidee/counta@5f1a523ada47aefcc7787f028483f880044c7bd1/evidence/live-verification.txt),
SHA-256 `48d94b3537b97d678e5d6c436ce686f7837140acfbc7aeadb74caabbb39739a4`.
Both were fetched as exact raw bytes and matched their commitments. They are
two URLs/hostnames but both fixtures are maintained in the same repository;
they are not independent authorship or provenance.

| Step | Transaction | Finalized result |
|---|---|---|
| `create_milestone` | [`0x0ce68af13b6fbc2af82c96a394344b0083238ad34e93be705ac14cf73438deb7`](https://explorer-studio.genlayer.com/tx/0x0ce68af13b6fbc2af82c96a394344b0083238ad34e93be705ac14cf73438deb7) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; state `funded`; value credited 0.001 GEN |
| `accept_milestone` | [`0x1da784e87a05de370f6bdbb2973fc611bca46dbd8569c2dbb11f74e0e0e1e473`](https://explorer-studio.genlayer.com/tx/0x1da784e87a05de370f6bdbb2973fc611bca46dbd8569c2dbb11f74e0e0e1e473) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; state `active` |
| `submit_delivery` | [`0x2126024b81059f8b2b3a4944d178678ee3f66f5c0ea6f11e3134506453b09f2e`](https://explorer-studio.genlayer.com/tx/0x2126024b81059f8b2b3a4944d178678ee3f66f5c0ea6f11e3134506453b09f2e) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; state `submitted`; committed URLs and hashes match |
| `review` | [`0x711c4da553cb11e78e41a6af951231cf25a58b8202fc37960d6c2bad40404730`](https://explorer-studio.genlayer.com/tx/0x711c4da553cb11e78e41a6af951231cf25a58b8202fc37960d6c2bad40404730) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; state `approved`, confidence 90 |
| `settle` | [`0xb9046fe756f09d16d87fe4c740cb9dcc6f2aa9db2e9b7f887eb7fd4a24ca334e`](https://explorer-studio.genlayer.com/tx/0xb9046fe756f09d16d87fe4c740cb9dcc6f2aa9db2e9b7f887eb7fd4a24ca334e) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; state `payout_dispatched`; ledger `deposited=0`; beneficiary amount 0.001 GEN |
| Child transfer | [`0x39882a964a1da3257544af0553e82de635a0dfd4363114ec535937fada0cc1bf`](https://explorer-studio.genlayer.com/tx/0x39882a964a1da3257544af0553e82de635a0dfd4363114ec535937fada0cc1bf) | FINALIZED; beneficiary received 0.001 GEN; `value_credited=true` |

The final canonical milestone read was `status=payout_dispatched`,
`settlement=beneficiary_payout_dispatched`, `deposited=0`,
`beneficiary_dispatched_amount=1000000000000000`, and sponsor amount 0. The
child receipt independently confirms the beneficiary credit. This is a
successful approval-and-payout proof, not a refund/timeout proof.

### Historical v0.3.0 release gate

Use Python 3.12 with the checked-in transitive constraints lock:

```powershell
python -m pip install -r requirements.txt -c requirements-lock.txt
python -m pytest tests/direct -q
python scripts/preflight.py
```

The gate checks exactly one deployable source (`contracts/counta.py`), Python
syntax/compilation, GenVM lint, generated ABI byte equality, and every Direct
Mode test with zero skips or failures. GitHub Actions installs with the same
lock and runs preflight on Ubuntu with the stock Direct Mode loader. Windows
alone receives the test stdin workaround. The workflow uses verified immutable
action commit references.

The v0.3.0 contract source was frozen at the commit/hash above and matched the
deployed source byte-for-byte at release. The documentation-only commit
`c821389a2a2e174356adda347bfbdcdc127d295b` did not change it. The v0.3.1
source is intentionally different; the v0.3.0 address continues to refer only
to its historical frozen bytes.

## Historical deployment: v0.2.0 (superseded)

| Evidence | Verified value |
|---|---|
| Network | GenLayer Studionet, chain ID 61999 |
| Frozen source commit | `dea00c4e656f74958ae3596c0de0934bae652b39` |
| Contract SHA-256 | `2fb1e76316fa4ae36ed3bbb3986cc2f4f4110dbef126e4706d520ad748b96b2a` |
| Source length | 30,854 bytes local and deployed |
| Contract address | [`0x8E1C18c660bf14d684ea5C1827D8d99BE27442f7`](https://explorer-studio.genlayer.com/address/0x8E1C18c660bf14d684ea5C1827D8d99BE27442f7) |
| Deployment transaction | [`0xbc0797477e26d1f0247ef91c301ed5a3b0a758bff89e50861521717b8949e485`](https://explorer-studio.genlayer.com/tx/0xbc0797477e26d1f0247ef91c301ed5a3b0a758bff89e50861521717b8949e485) |
| Deployment result | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS |
| Source parity | VERIFIED byte-for-byte with `gen_getContractCode`; SHA-256 equal |
| `get_info()` | Counta 0.2.0; minimum deposit `1000000000000000` wei; minimum confidence 75; text/image limits 16,000 / 2,000,000 bytes; three review and infrastructure attempts; 900-second retry cooldown |
| Release checks at frozen source commit | 47 Direct Mode tests passed; preflight, GenVM lint, ABI/schema passed; GitHub Actions run `37327672092` passed |
| Live lifecycle | Completed below; beneficiary child transfer independently verified `value_credited=true` |

### v0.2.0 live lifecycle

The sponsor was `0x865e118a3be4FA0760775565fCd31be156e1e3d7`; the designated
beneficiary was `0x2cd419603eBa593074653930Ddc4073d4FD8fc60`. The escrow was the
minimum 0.001 GEN (`1000000000000000` wei). The unique milestone ID was
`COUNTA-V020-LIVE-20261005-001`.

The deliverable fixture was 59 UTF-8 bytes from
[`https://raw.githubusercontent.com/Bibidee/counta/dea00c4e656f74958ae3596c0de0934bae652b39/evidence/live-deliverable.txt`](https://raw.githubusercontent.com/Bibidee/counta/dea00c4e656f74958ae3596c0de0934bae652b39/evidence/live-deliverable.txt),
SHA-256 `b2006a039e3ac90264b58902ea6a573fb18f8c4871f0e60af70555287d2eebe9`.
The separate repository-owned evidence fixture (not independently authored) was
82 UTF-8 bytes from
[`https://cdn.jsdelivr.net/gh/Bibidee/counta@dea00c4e656f74958ae3596c0de0934bae652b39/evidence/live-verification.txt`](https://cdn.jsdelivr.net/gh/Bibidee/counta@dea00c4e656f74958ae3596c0de0934bae652b39/evidence/live-verification.txt),
SHA-256 `48d94b3537b97d678e5d6c436ce686f7837140acfbc7aeadb74caabbb39739a4`.
Both URLs returned HTTP 200 and used distinct HTTPS hostnames. Distinct hostnames
were only transport separation; both artifacts came from the same repository,
so this is not proof of independent evidence provenance.

| Step | Transaction | Finalized result |
|---|---|---|
| `create_milestone` | [`0xe508ba728e0164c3c19b26176274c27bb4b2d2ee0e8dc7bfaf4be8fc9869bb52`](https://explorer-studio.genlayer.com/tx/0xe508ba728e0164c3c19b26176274c27bb4b2d2ee0e8dc7bfaf4be8fc9869bb52) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; state `funded`, deposit 0.001 GEN |
| `accept_milestone` | [`0x9293d8c1c68a2a458ed49e0aff0e3e3a7a75568b8b70be7f54d051095513d9f3`](https://explorer-studio.genlayer.com/tx/0x9293d8c1c68a2a458ed49e0aff0e3e3a7a75568b8b70be7f54d051095513d9f3) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; state `active` |
| `submit_delivery` | [`0xcef35b31c9a9e075b7a004f0a4f08cbfb447461f6f4907b208eb779f2af80607`](https://explorer-studio.genlayer.com/tx/0xcef35b31c9a9e075b7a004f0a4f08cbfb447461f6f4907b208eb779f2af80607) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; state `submitted`; committed URLs and hashes match |
| `review` | [`0xdc9a601abce30b5d65c00d64b50cc69b39c95d164b431caeed0880f97f955c46`](https://explorer-studio.genlayer.com/tx/0xdc9a601abce30b5d65c00d64b50cc69b39c95d164b431caeed0880f97f955c46) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; `approved`, confidence 100 |
| `settle` | [`0xfc0bac78a8e5dc8aed0f645c587fcc27c265148732b3a6e4e7555d9aee350de0`](https://explorer-studio.genlayer.com/tx/0xfc0bac78a8e5dc8aed0f645c587fcc27c265148732b3a6e4e7555d9aee350de0) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; `payout_dispatched`, ledger `deposited=0`, beneficiary amount 0.001 GEN |
| Child transfer | [`0x0a2289971dae55a32a0e751c05173473b5cb121dda3ba2e234460b7333f25f3f`](https://explorer-studio.genlayer.com/tx/0x0a2289971dae55a32a0e751c05173473b5cb121dda3ba2e234460b7333f25f3f) | FINALIZED; recipient is beneficiary, value 0.001 GEN, `value_credited=true` (child result `NO_MAJORITY`) |

The canonical final milestone read reports `status=payout_dispatched`,
`settlement=beneficiary_payout_dispatched`, `deposited=0`, and
`beneficiary_dispatched_amount=1000000000000000`. The beneficiary balance read
after the child transfer was 448.9979 GEN. Counta's status means the payout was
dispatched; the separate child receipt is the evidence that the transfer was
credited.

## Historical deployment: v0.1.0 (superseded)

This old deployment and lifecycle are retained as history. They demonstrate
v0.1.0 behavior only; they do not implement the v0.2.0 changes or prove v0.2.0
source parity.

```text
Network: GenLayer Studionet (chain ID 61999)
Contract: 0xF9e67Ff6f8a156a5357Ae8802402E11814B8887b
Explorer: https://explorer-studio.genlayer.com/address/0xF9e67Ff6f8a156a5357Ae8802402E11814B8887b
Deployment transaction: 0x70a708646708dc4cc171a49f79eb1dfe6c41e13ff02218fd9e826ae2906d2272
Transaction explorer: https://explorer-studio.genlayer.com/tx/0x70a708646708dc4cc171a49f79eb1dfe6c41e13ff02218fd9e826ae2906d2272
Status: FINALIZED; MAJORITY_AGREE (5 validator votes); GenVM SUCCESS
Historical source version: 0.1.0
Historical source SHA-256: d27387ed2f3522a37a642639221b840b9b9faf5426e2f0c079cbbf2a3addc4d5
Historical local/deployed byte length: 28,803 / 28,803
Historical source parity: VERIFIED byte-for-byte through gen_getContractCode
Historical frozen source commit: 06a9d62b600fb0e782c8bea940c4cb11a1fae376
```

The historical v0.1.0 live fixture `COUNTA-LIVE-20261005-001` used a 0.001
GEN deposit. Its completed root transactions were:

| Step | Transaction | Historical result |
|---|---|---|
| `create_milestone` | [0xdf57f8efce5952dd98316e11eee62cab3e772dacbcfa0d6cc39b2e408000b057](https://explorer-studio.genlayer.com/tx/0xdf57f8efce5952dd98316e11eee62cab3e772dacbcfa0d6cc39b2e408000b057) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; funded 1,000,000,000,000,000 wei |
| `submit_delivery` | [0xff822ce404f8489e48aa092b9cbd7642592b0d6341e1bdb854dd6d91dab09f66](https://explorer-studio.genlayer.com/tx/0xff822ce404f8489e48aa092b9cbd7642592b0d6341e1bdb854dd6d91dab09f66) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; submitted |
| `review` | [0xa990532e0dfae5325d506d96664e54bca1209423893c99a98dfca6b80e4aeac7](https://explorer-studio.genlayer.com/tx/0xa990532e0dfae5325d506d96664e54bca1209423893c99a98dfca6b80e4aeac7) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; approved, confidence 85 |
| `settle` | [0x472a821d53720d485f98ee06372f47d7fac94448aa3cce5af45a249e666b8447](https://explorer-studio.genlayer.com/tx/0x472a821d53720d485f98ee06372f47d7fac94448aa3cce5af45a249e666b8447) | FINALIZED / MAJORITY_AGREE / GenVM SUCCESS; v0.1.0 recorded settlement and emitted beneficiary transfer |

The historical sponsor was
`0x865e118a3be4fa0760775565fcd31be156e1e3d7`; the beneficiary was
`0x2cd419603eBa593074653930Ddc4073d4FD8fc60`. The pinned deliverable was
`https://raw.githubusercontent.com/Bibidee/counta/524ab720e10f632a6a038e58f89cefc169f85ae1/evidence/live-deliverable.txt`
with SHA-256 `b2006a039e3ac90264b58902ea6a573fb18f8c4871f0e60af70555287d2eebe9`.
The pinned evidence was
`https://cdn.jsdelivr.net/gh/Bibidee/counta@524ab720e10f632a6a038e58f89cefc169f85ae1/evidence/live-verification.txt`
with SHA-256 `48d94b3537b97d678e5d6c436ce686f7837140acfbc7aeadb74caabbb39739a4`.

### Historical child transfer observation

The v0.1.0 settle call emitted child transfer
[0x395dcd4d47ca6783e336899cc9f28012f77e531a2853dca6c20732a11c928f76](https://explorer-studio.genlayer.com/tx/0x395dcd4d47ca6783e336899cc9f28012f77e531a2853dca6c20732a11c928f76).
Its receipt was `FINALIZED`, result `NO_MAJORITY`, with `value_credited=true` for
1,000,000,000,000,000 wei. The observed beneficiary balance rose from 448.9959
to 448.9969 GEN. This is specifically a v0.1.0 observation, not evidence that
all future child transfers succeed.

## Historical v0.2.0 release gate (not evidence for v0.3.0)

The pinned package set is in `requirements.txt`. On Python 3.12 run:

```powershell
python -m pip install -r requirements.txt
python -m pytest tests/direct -q
python scripts/preflight.py
```

Preflight parses/compiles sources, checks that exactly one deployable contract
exists, runs GenVM lint, regenerates ABI into a temporary location and requires
byte equality with committed `artifacts/counta.abi.json`, then runs the genuine
Direct Mode tests. Any mismatch or failed check blocks release. CI invokes the
same preflight script.

The source was frozen at the commit and hash above before deployment. Release
checks and hosted CI passed on that source commit. The previous v0.1.0 address
below does not include v0.2.0 changes. The live table above records only
finalized transactions observed on the v0.2.0 address; no failure/refund or
uncertainty-exhaustion live flow is claimed here. Preserve child-transfer
receipts separately and do not infer recipient credit from `*_dispatched` state
alone.

The historical v0.2.0 policy required affirmative approval for beneficiary payment. Valid
semantic uncertainty was retryable twice and became `blocked` with
`semantic_uncertainty_sponsor_refund` on the third finalized uncertain review;
settlement then refunds the full ledger to the sponsor. Infrastructure failures
used their separate bounded budget and also ended sponsor-safe. In v0.2.0,
infrastructure-budget exhaustion could make the refund settleable early; v0.3.0
removes that behavior and requires review-deadline expiry. No Counta
`inconclusive` or split-payout state exists. GenLayer protocol outcomes such as
`Undetermined`, `LeaderTimeout`, and `ValidatorsTimeout` are not Counta
milestone states; they mean a review transaction did not finalize an adjudication.
Read canonical milestone state before taking action. If no adjudication
finalizes before the review deadline, permissionless `expire` performs the
deterministic sponsor refund without web or LLM access.
