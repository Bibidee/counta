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
5. **Dispatch:** only affirmative approval sends the full ledger to the
   beneficiary. Rejection, exhausted infrastructure failures, and exhausted
   semantic uncertainty refund the full ledger to the sponsor. All state debits
   happen before external transfer messages.
6. **Recover:** unaccepted/unsubmitted delivery expiry refunds the sponsor.
   Review-window expiry also refunds the sponsor if no accepted approval or
   rejection was reached.

## Security and accounting

- Raw response bytes are SHA-256 checked before text decoding or image review.
  Hash mismatch, bad HTTP status, empty/oversized content, invalid UTF-8 and
  unsupported images fail closed and cannot approve.
- Approval requires `deliverable_match=yes`, `evidence_support=yes`, `risk=no`,
  and confidence at least 75 in each validator's own analysis. Validators agree
  on the deterministic Counta outcome (`approved`, `blocked`, or `retryable`),
  not matching rationale, confidence numbers, or diagnostic enum details.
  The stored leader confidence is descriptive, while each validator's confidence
  is used only for that validator's own 75-point approval gate. Rationale is
  informational and never controls authorization. Missing/invalid confidence is
  normalized to zero; malformed decision enums or unparseable output fail closed.
- Artifact and evidence contents are untrusted prompt data. Images are raw PNG
  or JPEG only; text and evidence must be UTF-8.
- Infrastructure failures and malformed model output consume only the separate
  infrastructure budget. After three finalized such failures, the milestone is
  blocked and sponsor-refund eligible. Valid semantic uncertainty has its own
  three-attempt budget: the first two results remain retryable after cooldown;
  the third blocks and makes the full escrow sponsor-refund eligible. Neither
  uncertainty nor infrastructure failure can cause beneficiary payment.
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

## Integrator safeguards for platform boundaries

These are operational requirements, not guarantees the contract can create:

- **Artifact destinations:** integrators should admit only expected public HTTPS
  hosts and immutable, commit-pinned paths before calling Counta. Avoid redirect
  URLs and user-controlled shorteners. Counta validates URL syntax and rejects
  private IP literals, but GenLayer's current web response does not expose a
  redirect chain/final URL or a redirect-disable option to the contract; DNS
  resolution and redirect destinations therefore remain platform/network trust
  boundaries. Exact-byte hashes still make changed content fail closed.
- **Consensus:** wait for the canonical transaction status. `UNDETERMINED` is
  not an application verdict and does not authorize settlement; inspect the
  milestone state before retrying, and respect the contract's retry cooldown and
  attempt budgets. Never reinterpret a missing/undetermined result as approval.
- **Transfers:** treat a terminal `*_dispatched` state as an emitted payout or
  refund instruction, not proof of recipient credit. Follow the parent
  transaction's child transfer to its final result and verify `value_credited`
  where exposed. Do not submit a second settlement or infer a refund after an
  ambiguous/pending child result; resolve it from the canonical receipt first.
- **Storage:** plan for permanent on-chain history and its cost. Keep an
  off-chain indexed archive for search/analytics, but treat chain state and
  finalized receipts as authoritative. For independent workloads, consider
  separate Counta deployments/cohorts so one deployment's history and growth
  are operationally bounded; this does not erase historical chain data.

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
