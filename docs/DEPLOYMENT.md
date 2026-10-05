# Counta deployment and evidence

## Current release candidate: v0.2.0 — not deployed

The hardened local source changes escrow lifecycle and storage-visible state,
so the previous Studionet deployment is not a deployment of this source. No
v0.2.0 address, deployment transaction, or source-parity claim exists yet.

| Evidence | v0.2.0 value |
|---|---|
| Frozen source commit | Pending release freeze |
| Contract SHA-256 | Pending release freeze |
| Studionet address / deployment tx | Not deployed |
| Deployed source parity | Not applicable yet |
| Live v0.2.0 lifecycle | Not run |

Do not submit the historical address below as evidence for v0.2.0. A fresh
deployment and raw deployed-source parity check are required after source freeze.

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

## v0.2.0 release gate and deployment procedure

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

After freezing v0.2.0 source, record its commit and raw SHA-256, deploy only
`contracts/counta.py` to Studionet, wait for finalization, check `get_info()`
reports `0.2.0`, retrieve the deployed raw source with `gen_getContractCode`
or equivalent and compare bytes. Then run a fresh lifecycle exercising
create → accept → submit → review → dispatch, plus failure/refund and eligible
semantic uncertainty behavior. Preserve child-transfer receipts separately.
Update the v0.2.0 table above only with observed results. Do not infer successful
recipient credit from Counta's `*_dispatched` state alone: verify each emitted
child transfer receipt/result and `value_credited` when available.
