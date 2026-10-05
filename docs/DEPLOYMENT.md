# Deployment and verification

Counta v0.1.0 is a local pre-deployment candidate. **It has not been deployed**
to Studionet or another network. No deployment address, transaction, or live
semantic result is claimed.

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

The present repository state has not completed these live steps.
