# Counta deployment and release evidence

## Current candidate: v0.3.0 — NOT DEPLOYED

The v0.3.0 source is a pre-deployment candidate. It has no contract address,
deployment transaction, live lifecycle, or source-parity claim. Do not attribute
the historical address below to v0.3.0. The candidate adds sponsor-bound
evidence-host admission, sponsor-scoped milestone references, and deadline-only
refund after infrastructure retry exhaustion.

Frozen candidate source SHA-256: `1c3e41f9354ae8dd682d8d7d9e5f4062ac7db8ce647eaca7c3ea27eb9808379e`
(36,339 bytes). This identifies the current source candidate only; it is not a
deployment/source-parity assertion.

The v0.2.0 Studionet deployment and its live transactions remain below as
historical evidence. That deployment does **not** contain v0.3.0 fixes.

### v0.3.0 release gate

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

Before any future deployment, require a clean frozen commit and successful
GitHub Actions on that exact SHA; record the commit's contract SHA-256; tag the
source; deploy only those exact bytes; retrieve and compare deployed source;
verify `get_info()`; and record finalized live approval/refund lifecycle plus
each child transfer receipt and `value_credited`. No v0.3.0 tag or deployment
was created by this task.

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
