# Deployment and verification

Counta v0.1.0 is deployed to GenLayer Studionet. This section records deployment
and source provenance only; a live milestone review and escrow transfer have
not yet been demonstrated.

## Verified deployment

```text
Network: GenLayer Studionet (chain ID 61999)
Contract: 0xF9e67Ff6f8a156a5357Ae8802402E11814B8887b
Explorer: https://explorer-studio.genlayer.com/address/0xF9e67Ff6f8a156a5357Ae8802402E11814B8887b
Deployment transaction: 0x70a708646708dc4cc171a49f79eb1dfe6c41e13ff02218fd9e826ae2906d2272
Transaction explorer: https://explorer-studio.genlayer.com/tx/0x70a708646708dc4cc171a49f79eb1dfe6c41e13ff02218fd9e826ae2906d2272
Transaction status: FINALIZED
Consensus: MAJORITY_AGREE (5 validator votes agree)
GenVM execution: SUCCESS
Source version: 0.1.0
Source SHA-256: d27387ed2f3522a37a642639221b840b9b9faf5426e2f0c079cbbf2a3addc4d5
Local / deployed bytes: 28,803 / 28,803
Source parity: VERIFIED byte-for-byte through gen_getContractCode
```

The read-only `get_info()` result reports `name=Counta`, `version=0.1.0`,
`min_confidence=75`, `min_deposit=1000000000000000`, and the configured limits.
The exact frozen deployment source is commit `06a9d62b600fb0e782c8bea940c4cb11a1fae376`.

The pushed release commit's [GitHub Actions run](https://github.com/Bibidee/counta/actions/runs/37259378417)
completed successfully. Its release gate ran the pinned Direct Mode tests,
GenVM lint, and schema generation.

## Release gate

Use Python 3.12 and the pinned dependencies:

```powershell
python -m pip install -r requirements.txt
python scripts/preflight.py
```

The preflight parses/compiles source and tests, runs all official Direct Mode
tests, checks the one deployable contract with GenVM lint, and regenerates the
ABI at `artifacts/counta.abi.json`. Missing tools or any failed command are a
release failure, not a skipped check.

Before deployment, freeze the source in a commit and record its SHA-256. Deploy
only `contracts/counta.py` with the current supported GenLayer deployment
tooling. A successful deployment requires a finalized transaction, successful
GenVM execution, `get_info()` reporting Counta v0.1.0, and byte-for-byte source
parity through a supported raw source retrieval method. Do not claim source
parity if raw deployed source cannot be retrieved and compared.

## Live milestone lifecycle

Fixture `COUNTA-LIVE-20261005-001` completed on the deployed contract using a
0.001 GEN deposit. Each root transaction below finalized with `MAJORITY_AGREE`
and GenVM `SUCCESS`:

| Step | Transaction | Canonical result |
|---|---|---|
| `create_milestone` | [0xdf57f8efce5952dd98316e11eee62cab3e772dacbcfa0d6cc39b2e408000b057](https://explorer-studio.genlayer.com/tx/0xdf57f8efce5952dd98316e11eee62cab3e772dacbcfa0d6cc39b2e408000b057) | `funded`, `deposited=1000000000000000` wei |
| `submit_delivery` | [0xff822ce404f8489e48aa092b9cbd7642592b0d6341e1bdb854dd6d91dab09f66](https://explorer-studio.genlayer.com/tx/0xff822ce404f8489e48aa092b9cbd7642592b0d6341e1bdb854dd6d91dab09f66) | `submitted`; pinned URLs and both hashes match |
| `review` | [0xa990532e0dfae5325d506d96664e54bca1209423893c99a98dfca6b80e4aeac7](https://explorer-studio.genlayer.com/tx/0xa990532e0dfae5325d506d96664e54bca1209423893c99a98dfca6b80e4aeac7) | `approved`, confidence `85` |
| `settle` | [0x472a821d53720d485f98ee06372f47d7fac94448aa3cce5af45a249e666b8447](https://explorer-studio.genlayer.com/tx/0x472a821d53720d485f98ee06372f47d7fac94448aa3cce5af45a249e666b8447) | `settled`, `pay_beneficiary`, deposited `0`, beneficiary amount `1000000000000000` wei |

Sponsor: `0x865e118a3be4fa0760775565fcd31be156e1e3d7`. Beneficiary:
`0x2cd419603eBa593074653930Ddc4073d4FD8fc60`.

The exact-byte deliverable URL is
`https://raw.githubusercontent.com/Bibidee/counta/524ab720e10f632a6a038e58f89cefc169f85ae1/evidence/live-deliverable.txt`
with SHA-256
`b2006a039e3ac90264b58902ea6a573fb18f8c4871f0e60af70555287d2eebe9`.
The verification URL is
`https://cdn.jsdelivr.net/gh/Bibidee/counta@524ab720e10f632a6a038e58f89cefc169f85ae1/evidence/live-verification.txt`
with SHA-256
`48d94b3537b97d678e5d6c436ce686f7837140acfbc7aeadb74caabbb39739a4`.

### Transfer receipt detail

The settle transaction emitted one GEN transfer to the beneficiary. The child
transaction is
[0x395dcd4d47ca6783e336899cc9f28012f77e531a2853dca6c20732a11c928f76](https://explorer-studio.genlayer.com/tx/0x395dcd4d47ca6783e336899cc9f28012f77e531a2853dca6c20732a11c928f76).
Its receipt is `FINALIZED` with result `NO_MAJORITY`, but `value_credited=true`
for `1000000000000000` wei. The beneficiary’s public account balance was
448.9959 GEN before the flow and 448.9969 GEN after it, confirming the 0.001
GEN credit. This child-transaction result is an explicit platform observation;
it is not described as `MAJORITY_AGREE`.

The committed evidence artifacts are pinned to Git commit
`524ab720e10f632a6a038e58f89cefc169f85ae1`. The final lifecycle evidence and
updated docs do not modify `contracts/counta.py`.
