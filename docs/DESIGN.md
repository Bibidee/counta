# Counta protocol design (v0.2.0)

Counta is a reusable milestone escrow primitive. Funding terms, parties and the
delivery deadline are fixed when the sponsor deposits GEN. The beneficiary must
explicitly accept before doing the committed work. One text/image deliverable
and its textual evidence are then pinned by URL and exact raw-byte SHA-256.
GenLayer validators independently fetch and verify those bytes and judge them
against the immutable brief. Deterministic code—not model rationale—controls
the state transition and escrow dispatch.

## State and transitions

| Current state | Trigger / condition | Next state | Ledger and disposition |
|---|---|---|---|
| — | Sponsor creates with payable value | `funded` | Exact `gl.message.value` held |
| `funded` | Named beneficiary accepts before deadline | `active` | No ledger movement; terms unchanged |
| `funded` | Sponsor cancels before acceptance | `refund_dispatched` | Ledger zeroed; full sponsor refund message emitted |
| `funded` or `active` | `now >= deliver_by`, no submission | `refund_dispatched` | Ledger zeroed; full sponsor refund message emitted |
| `active` | Beneficiary submits once while `now < deliver_by` | `submitted` | Hashes and URLs fixed; review deadline starts |
| `submitted` / `retryable` | Agreed strict safe tuple, confidence >= 75 | `approved` | Funds remain held pending dispatch |
| `submitted` / `retryable` | Agreed substantive rejection or artifact integrity failure | `blocked` | Funds remain held pending sponsor refund dispatch |
| `submitted` / `retryable` | Valid, hash-verified semantic result is uncertain | `retryable` or `inconclusive` | Counts against semantic budget; third such result produces `inconclusive` |
| `submitted` / `retryable` | Fetch/provider/LLM/malformed-output failure | `retryable` or `blocked` | Separate infrastructure budget; third failure is sponsor-refund eligible |
| `submitted` / `retryable` | `now >= review_deadline` before `inconclusive` | `refund_dispatched` | Sponsor receives full ledger; never a timeout split |
| `approved` | Anyone calls `settle` | `payout_dispatched` | Ledger zeroed; full beneficiary transfer message emitted |
| `blocked` | Anyone calls `settle` | `refund_dispatched` | Ledger zeroed; full sponsor transfer message emitted |
| `inconclusive` | Anyone calls `settle` | `split_dispatched` | Ledger zeroed; exact 50/50 split messages emitted; odd wei to beneficiary |

Dispatched states are terminal. No second settlement/expiry call can dispatch
the same ledger again. Sponsor cancellation becomes unavailable once the
beneficiary accepts. The deadline is measured from creation, not acceptance.

## Review budgets and economic policy

Only the sponsor or named beneficiary can trigger `review`; unrelated callers
cannot consume any review budget. Every finalized retryable outcome sets a
15-minute cooldown. Valid semantic uncertainty increments `semantic_attempts`.
After three such results, `INCONCLUSIVE` permits the pre-agreed 50/50 split.
The split is therefore reachable only after three valid structured semantic
analyses based on artifacts that were fetched, size-checked, hash-verified and
decoded/validated successfully.

Infrastructure failures have a separate three-attempt budget and never count
as semantic uncertainty. This includes unavailable fetches (429/5xx/network),
LLM execution failures, malformed model output and invalid consensus results.
After three such finalized outcomes, Counta moves to `blocked`, which is
sponsor-refund eligible. If the review deadline expires first while the
milestone is still `submitted` or `retryable`, `expire` also dispatches the full
ledger to the sponsor. Thus beneficiary-controlled source outages cannot earn
a split. Integrity failures (hash mismatch, non-success HTTP response, empty
or oversized bytes, invalid UTF-8, unsupported image type) fail closed as
`blocked` and are sponsor-refund eligible.

This policy intentionally places persistent evidence/provider availability
risk on the beneficiary for payout purposes while preserving deterministic
refund recovery. It does not establish which party caused a network failure.

## Semantic consensus and artifact binding

`run_nondet_unsafe` runs the same observation pipeline for leader and
validators. The contract snapshots storage-backed review inputs before entering
the nondeterministic callback. The callback fetches exact response bytes,
verifies SHA-256 commitments, validates bounded UTF-8/image representations,
then invokes `exec_prompt`. Untrusted brief, summary, deliverable and evidence
are framed as data; instructions inside them must not be followed.

Approval requires every accepted analysis to resolve to the same exact enum
tuple (`deliverable_match`, `evidence_support`, `risk`) and final authorization
decision. Confidence may vary by at most 20 points; rationale text is not
compared. Approval is only `yes / yes / no` with confidence >= 75. A malformed
output or disagreement never approves. SHA-256 binds bytes, not authorship,
truth or real-world completion.

## Escrow ledger and transfer messages

`deposited` is the sole escrow ledger, initialized only from `gl.message.value`.
Every terminal dispatch copies amounts into explicit `*_dispatched_amount`
fields, zeros `deposited`, records a terminal `*_dispatched` status, and only
then emits the external transfer message through `_send_gen`. Repeated dispatch
is rejected because the ledger is zero and the status is terminal.

The contract cannot synchronously observe whether a child value-transfer
transaction was finally credited. A dispatched status proves Counta recorded
the debit and emitted transfer message(s), not that each recipient received
value. Integrators must verify child receipts/results and `value_credited` where
the network exposes it. There is no unsupported callback or false “paid” flag.

## Capacity and trust boundaries

There is no fixed lifetime milestone cap; cancelling/expiring records cannot
consume a global 256-entry quota. Historical TreeMap records are retained, so
chain-level storage constraints/costs still bound practical use. No admin
backdoor, appeal role, ERC-20 support or cross-chain payout exists.

URLs are restricted to HTTPS on port 443 without credentials/fragments and
reject local and non-public IP-literal targets. Static checks cannot guarantee
DNS answers, redirects, provider behavior or consistent external availability
for every validator. GenLayer consensus may disagree or remain undetermined;
Counta does not promise to suppress that platform outcome.
