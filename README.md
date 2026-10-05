# Counta

Counta is a standalone GenLayer Intelligent Contract primitive for milestone
evidence escrow. A sponsor funds a fixed brief and names a beneficiary. The
beneficiary accepts the terms, then submits one text or image deliverable and
textual evidence committed by exact-byte SHA-256 hashes. Validators independently
fetch and verify the artifacts before semantically assessing the deliverable.
Deterministic contract logic controls authorization, review budgets, deadlines,
escrow accounting and transfer dispatch.

Counta is an escrow primitive—not a frontend, marketplace, identity provider,
or guarantee that work is truthful or legally compliant.

## Why GenLayer?

Ordinary deterministic contract code cannot reliably decide whether an
unstructured file, photograph or supporting evidence substantively satisfies a
natural-language milestone brief. Counta uses GenLayer's independent validator
observations and semantic review for that narrow judgment. No single off-chain
decision service is trusted to authorize payout. The contract still does not
eliminate validator disagreement, unavailable providers or `UNDETERMINED`
consensus outcomes.

## Lifecycle

1. **Fund:** sponsor calls payable `create_milestone`; exact `gl.message.value`
   becomes the escrow ledger.
2. **Accept:** only the named beneficiary may call `accept_milestone`. The sponsor
   can cancel only before this acceptance. The delivery deadline is fixed at
   creation and is not extended by acceptance.
3. **Submit:** accepted beneficiary submits once, strictly before `deliver_by`,
   committing distinct-host HTTPS URLs and SHA-256 hashes.
4. **Review:** only sponsor or beneficiary may trigger review. Retries have a
   15-minute cooldown and separate bounded semantic/infrastructure counters.
5. **Dispatch:** approved sends the full ledger to the beneficiary; substantive
   rejection or exhausted infrastructure failures refund the sponsor; only
   three valid, hash-verified semantic uncertainty results may reach the 50/50
   uncertainty split. All state debits happen before external transfer messages.
6. **Recover:** unaccepted/unsubmitted delivery expiry refunds the sponsor.
   Review-window expiry also refunds the sponsor unless valid semantic
   uncertainty already reached `INCONCLUSIVE`.

## Security and accounting

- Raw response bytes are SHA-256 checked before text decoding or image review.
  Hash mismatch, bad HTTP status, empty/oversized content, invalid UTF-8 and
  unsupported images fail closed and cannot approve.
- Approval requires `deliverable_match=yes`, `evidence_support=yes`, `risk=no`,
  confidence at least 75, and validator agreement on the bounded semantic tuple
  with confidence values no more than 20 points apart. Rationale wording is not
  consensus-critical.
- Artifact and evidence contents are untrusted prompt data. Images are raw PNG
  or JPEG only; text and evidence must be UTF-8.
- Infrastructure failures and malformed model output consume only the separate
  infrastructure budget. After three finalized such failures, the milestone is
  sponsor-refund eligible; these failures never cause beneficiary payment or a
  split. A retry cooldown applies. Only valid semantic uncertainty can split.
- The beneficiary must accept before sponsor cancellation is locked. `deliver_by`
  is measured from creation; submission is valid only while `now < deliver_by`,
  while expiry is valid at `now >= deliver_by`. Review follows the same strict
  boundary at `review_deadline`.
- Contract-level milestone count has no fixed lifetime cap. Historical records
  remain stored, so chain/storage limits and costs still apply.
- Terminal statuses say `*_dispatched`, not “paid” or “settled”. Counta debits
  its escrow ledger and emits external GEN transfer messages, but cannot observe
  a recipient's child-transfer credit through a reliable callback. Integrators
  must inspect each child transaction/result, including `value_credited`, before
  treating the beneficiary or sponsor as paid.
- HTTPS syntax checks cannot guarantee public DNS resolution or safe redirect
  behavior at every validator. SHA-256 proves byte identity, not provenance or
  truth. Model confidence is not a calibrated probability.

## Release status

- Current source: **v0.2.0, not deployed**. The existing Studionet v0.1.0
  deployment below is historical and does not contain these changes.
- Deployable contract sources: exactly `contracts/counta.py`.
- No frontend or additional trusted service is required.
- v0.2.0 source parity, deployment and live lifecycle evidence: **pending**.

Historical v0.1.0 deployment and its verified live lifecycle are preserved in
[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md). Do not present that address, old source
hash or lifecycle as proof of v0.2.0.

## Build and test

Use Python 3.12 and pinned dependencies:

```powershell
python -m pip install -r requirements.txt
python -m pytest tests/direct -q
python scripts/preflight.py
```

Preflight compiles the source/tests, runs GenVM lint, regenerates and compares
the ABI against the committed artifact, and executes the official pinned
GenLayer Direct Mode tests against the actual contract. CI runs the same gate.
