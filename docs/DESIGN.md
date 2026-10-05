# Counta design

Counta is a standalone milestone-evidence escrow primitive. The sponsor funds
the escrow with native GEN when creating the milestone. The contract records
the actual `gl.message.value` as the sole payout ledger, separately from the
milestone terms. A designated beneficiary may submit exactly one deliverable
and supporting evidence package. The immutable brief, parties, amount, and
deadlines cannot be edited after funding.

## Review model

The contract fetches the committed artifact and evidence itself. It hashes the
exact raw response bytes with SHA-256 before decoding text or passing raw PNG or
JPEG bytes to GenLayer's image-capable prompt interface. A successful review
requires independently repeated observation and agreement on the exact semantic
tuple `deliverable_match`, `evidence_support`, and `risk`; the confidence values
must be within 20 points and must derive the same authorization outcome.
Rationale is explanatory only. `APPROVED` requires `yes / yes / no` and
confidence of at least 75. Explicit contradiction or failure is `BLOCKED`;
uncertainty, low confidence, transient fetch failure, and malformed model
output are non-approving and retryable. After three finalized non-approving
reviews the milestone becomes `INCONCLUSIVE`.

All artifacts, briefs, summaries, and evidence are untrusted content. The
prompt states that artifact instructions are data, not instructions. Image
support is limited to raw PNG/JPEG deliverables; evidence remains UTF-8 text.

## Lifecycle and escrow outcomes

| From | Trigger | To / accounting |
|---|---|---|
| — | Sponsor creates payable milestone | `FUNDED`; exact `gl.message.value` held |
| `FUNDED` | Beneficiary submits once before `deliver_by` | `SUBMITTED`; brief/parties/funds unchanged |
| `FUNDED` | Sponsor cancels before submission | `CANCELLED`; full refund to sponsor |
| `FUNDED` | Deadline passes without delivery; anyone calls `expire` | `EXPIRED`; full refund to sponsor |
| `SUBMITTED` / `RETRYABLE` | Agreed semantic approval | `APPROVED`; funds remain held until settlement |
| `SUBMITTED` / `RETRYABLE` | Agreed substantive rejection or integrity failure | `BLOCKED`; funds remain held until settlement |
| `SUBMITTED` / `RETRYABLE` | Uncertainty, malformed output, or transient failure | `RETRYABLE`, up to three finalized attempts; then `INCONCLUSIVE` |
| `APPROVED` | Anyone calls `settle` | `SETTLED`; full amount emitted to beneficiary |
| `BLOCKED` | Anyone calls `settle` | `SETTLED`; full amount refunded to sponsor |
| `INCONCLUSIVE` | Anyone calls `settle` | `SETTLED`; 50/50 split, odd wei remainder to beneficiary |
| `SUBMITTED` / `RETRYABLE` | Review deadline passes; anyone calls `expire` or `settle` | `SETTLED`; same 50/50 split |

Every settlement reads the deposited ledger, sets it to zero and records the
one-time disposition before emitting GEN. A second settlement has no positive
ledger to pay. Sponsor cancellation is possible only before the beneficiary
submits. The beneficiary cannot overwrite a submitted artifact.

The 50/50 unresolved-review rule is an explicit risk allocation, not a claim
that the contract can determine which party is right when consensus is
unavailable. Participants must agree to it before funding. It ensures a
deterministic, bounded exit rather than indefinitely locked funds.

## Security boundaries

- SHA-256 commitments bind review to exact fetched bytes; mismatch never
  approves.
- URLs must use HTTPS, port 443, and a syntactically valid hostname; localhost,
  `.local`, and non-public IP literals are rejected. The contract cannot
  reliably resolve DNS or guarantee redirect behavior, so URL admission is not
  a complete network-layer SSRF defense.
- A hash proves byte identity, not truth, authorship, completion, or legal
  compliance.
- The LLM/validator decision is semantic evidence assessment, not an oracle or
  guarantee of real-world performance. Validators may disagree and transactions
  may remain unfinalized under GenLayer consensus.
- The model's bounded confidence is not a calibrated probability.
- The escrow holds native GEN only; it does not support ERC-20 tokens or
  cross-chain payouts.
- A finalized contract settlement records the outcome and emits native-value
  transfers. Integrators should also inspect the finalized transfer/message
  results on the selected network.
- Capacity is limited to 256 lifetime milestones; records are not deleted.
- No post-review appeal/challenge flow exists in v0.1.0. Parties accept the
  published review and timeout rules when funding.
