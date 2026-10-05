# Counta deployment and release evidence

## Current deployed release: v0.3.1

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
creation until acceptance. This records deployment and exact source parity;
it does not claim a fresh v0.3.1 live milestone review, payout, outage-recovery,
or refund/timeout lifecycle. The v0.3.0 lifecycle below remains historical.

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
