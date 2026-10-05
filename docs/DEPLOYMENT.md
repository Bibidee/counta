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

## Suggested live verification

1. Create the milestone with a payable amount and confirm `deposited` equals
   the attached value exactly.
2. Submit a simple immutable HTTPS deliverable and evidence pair; independently
   hash their exact raw bytes.
3. Read the milestone and verify the parties, brief, URLs, commitments, and
   `submitted` status.
4. Run `review`, record its finalized consensus and GenVM execution status,
   then inspect the canonical state.
5. Only if it is genuinely `approved`, call `settle` and verify the beneficiary
   transfer and zeroed ledger. For `blocked`, verify the sponsor refund. For
   `inconclusive` or deadline expiry, verify both split transfers.
6. Attempt a second settlement only as a negative check; it must fail without
   another payment.

These milestone lifecycle steps remain future live verification. Deployment
finality and source parity do not establish that semantic review or GEN payouts
have been exercised on this contract.
