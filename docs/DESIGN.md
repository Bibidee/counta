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
| `submitted` / `retryable` | Agreed strict safe tuple; each analysis confidence >= 75 | `approved` | Funds remain held pending full beneficiary dispatch |
| `submitted` / `retryable` | Agreed substantive rejection or artifact integrity failure | `blocked` | Funds remain held pending full sponsor refund dispatch |
| `submitted` / `retryable` | Valid, hash-verified semantic result is uncertain | `retryable` for attempts 1–2; `blocked` on attempt 3 | Third result reason is `semantic_uncertainty_sponsor_refund`; full sponsor refund |
| `submitted` / `retryable` | Fetch/provider/LLM/malformed-output failure | `retryable` or `blocked` | Separate infrastructure budget; third failure is sponsor-refund eligible |
| `submitted` / `retryable` | `now >= review_deadline` | `refund_dispatched` | Sponsor receives full ledger |
| `approved` | Anyone calls `settle` | `payout_dispatched` | Ledger zeroed; full beneficiary transfer message emitted |
| `blocked` | Anyone calls `settle` | `refund_dispatched` | Ledger zeroed; full sponsor transfer message emitted |

Dispatched states are terminal. No second settlement/expiry call can dispatch
the same ledger again. Sponsor cancellation becomes unavailable once the
beneficiary accepts. The deadline is measured from creation, not acceptance.

## Review budgets and economic policy

Only the sponsor or named beneficiary can trigger `review`; unrelated callers
cannot consume any review budget. Every finalized retryable outcome sets a
15-minute cooldown. Valid semantic uncertainty increments `semantic_attempts`.
The first two finalized uncertain analyses leave the milestone `retryable`.
The third sets `blocked` with reason
`semantic_uncertainty_sponsor_refund`. The beneficiary is paid only after an
affirmative `approved` outcome; uncertainty never authorizes a partial payout.

Infrastructure failures have a separate three-attempt budget and never count
as semantic uncertainty. This includes unavailable fetches (429/5xx/network),
LLM execution failures, malformed model output and invalid consensus results.
After three such finalized outcomes, Counta moves to `blocked`, which is
sponsor-refund eligible. If the review deadline expires first while the
milestone is still `submitted` or `retryable`, `expire` also dispatches the full
ledger to the sponsor. Thus beneficiary-controlled source outages cannot earn
beneficiary payment. Integrity failures (hash mismatch, non-success HTTP response, empty
or oversized bytes, invalid UTF-8, unsupported image type) fail closed as
`blocked` and are sponsor-refund eligible.

This policy intentionally places persistent evidence/provider availability
risk on the beneficiary for payout purposes while preserving deterministic
refund recovery. It does not establish which party caused a network failure.
`INCONCLUSIVE`, `SPLIT_DISPATCHED`, and uncertainty-based split settlement are
not Counta states or economic outcomes.

## Semantic consensus and artifact binding

`run_nondet_unsafe` runs the same observation pipeline for leader and
validators. The contract snapshots storage-backed review inputs before entering
the nondeterministic callback. The callback fetches exact response bytes,
verifies SHA-256 commitments, validates bounded UTF-8/image representations,
then invokes `exec_prompt`. Untrusted brief, summary, deliverable and evidence
are framed as data; instructions inside them must not be followed.

Equivalence compares a deterministic canonical outcome: `approved`, `blocked`,
or `retryable` for valid analyses; `integrity_failure` for integrity errors; and
`error` for infrastructure/model errors. The validator independently reruns
fetching and semantic analysis as before. Different enum diagnostics, confidence
values, rationale strings, or bounded error classes are equivalent only when
they have the same canonical outcome. In particular, an `approved` outcome is
possible only if each observation independently has
`deliverable_match=yes`, `evidence_support=yes`, `risk=no`, and confidence >= 75.
A confidence of 74 cannot validate an approval at 90; 80 and 97 can, because
both independently pass the unchanged threshold. The stored leader confidence
is descriptive after that per-observation gate; rationale is informational only.
Missing/invalid confidence is normalized to zero (never approval), and malformed
decision enums or unparseable output fail closed. Metadata variance does not
create another consensus gate. SHA-256 binds bytes, not authorship, truth or
real-world completion.

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

## Required integration safeguards

Integrators should apply a public-host allowlist and prefer immutable,
commit-pinned HTTPS artifact paths; avoid shorteners and redirect URLs. The
contract-side web response exposes the fetched response but not a final URL or
redirect chain, and the request API has no documented redirect-disable control,
so the contract cannot independently prove DNS/redirect safety. Hash verification
still rejects bytes that differ from the committed content.

An `UNDETERMINED` transaction is not a milestone verdict and must never be
treated as authorization to release funds. Integrators must read canonical state
before any retry and obey Counta's cooldown and bounded retry budgets.
GenLayer transaction outcomes such as `Undetermined`, `LeaderTimeout`, and
`ValidatorsTimeout` belong to the protocol lifecycle, not Counta's state
machine. An `Undetermined` review means only that the transaction did not
finalize an adjudication; Counta state remains unchanged. Where supported,
integrators may use the protocol's leader-appeal/retry path, and otherwise rely
on the deterministic Counta review-deadline refund. The expiry path performs no
web fetch or LLM call.

After a terminal dispatch, integrators must follow the emitted child transfer
through finality and inspect its result and `value_credited` where available.
Do not call settlement again to compensate for an ambiguous child result: the
parent ledger is intentionally already zero, and an unverified retry could
duplicate payment. Escalate unresolved child-transaction failures using the
network's receipt/support process.

Historical milestones remain in persistent contract storage by design. Plan
for their storage cost, use an off-chain indexer for search, and treat finalized
on-chain state as authoritative. Separate deployments can isolate workloads,
but cannot erase chain history or remove storage cost from an existing record.
