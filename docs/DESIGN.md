# Counta protocol design (v0.3.1)

Counta holds sponsor-provided GEN against one fixed milestone. The sponsor
commits the parties, brief, delivery deadline, review window and exact allowed
evidence hostname before beneficiary acceptance. A single hash-bound submission
is independently fetched and semantically assessed through GenLayer. Only
deterministic state logic releases funds.

v0.3.1 is the current deployed Studionet release at
`0xE4Bb7FC4C217EE867F14d40aFaa1e868693CDcAB`. Its frozen source commit is
`8c7d472522e90b481bce56794c175e2e951c99fa`; the contract SHA-256 is
`9b98e0016a38e7c4ad8e613370b0667e7c4b37910e4dbaf26e99a6a1688be005` and
contains 36,535 bytes. Deployed-source parity was verified byte-for-byte.
v0.3.0 remains historical and superseded at
`0x4235915E7ec84596239b2d29B93d1a2A982A1018`; its approval/payout evidence is
preserved in `docs/DEPLOYMENT.md`. That version used a shared three-failure
infrastructure ceiling: after three temporary failures, further review was
locked out until deadline expiry. v0.3.1 removes that liveness lockout.

## Identity and evidence authority

The sponsor-local ID is not globally unique. Counta stores each record under a
canonical reference derived from the normalized sponsor address and local ID:

```text
0x<sponsor-address-lowercase>:<sponsor-local-id>
```

`create_milestone` returns that canonical reference. Subsequent methods accept
it, so integrations never need to guess which sponsor namespace a local name
means. The sponsor alias is registered at creation. A beneficiary alias is
registered only when the named beneficiary accepts; until then the beneficiary
must use the canonical reference. If an accepted party-local alias collides,
that alias becomes ambiguous and callers must use the composite reference.
This prevents an unrelated sponsor from poisoning a wallet's alias merely by
nominating that wallet as beneficiary. The scoped storage key prevents
unrelated wallets from reserving another sponsor's ID. Historical records are
not deleted. Because local IDs may contain `:`, an ID that syntactically
resembles a canonical reference can be parsed as one before party-local alias
lookup. Integrations should store and use the canonical `milestone_ref`
returned by `create_milestone` rather than relying on party-local aliases for
arbitrary user-supplied IDs.

When creating the milestone, the sponsor chooses one exact evidence hostname.
It is normalized to lowercase and strips one or more trailing dots; schemes,
ports, paths, userinfo, percent escapes, Unicode hostnames, IP literals, local
names and malformed DNS labels are rejected. There are no wildcards or suffix
matches. Submission-time URL parsing applies the same hostname normalization,
then requires exact equality with the immutable sponsor policy. A URL on a
different CDN or a hostname such as `trusted.example.attacker.test` cannot
satisfy `trusted.example`.

This is a sponsor-selected authority policy, not an identity oracle. A sponsor
may choose a host controlled by the beneficiary; Counta cannot prove who
authored it. A matching hostname plus SHA-256 proves only that validators
retrieved the committed bytes from a URL on the chosen host, not that the
contents are accurate or independently authored.

## State machine and deadline boundaries

| State | Trigger | Next state | Economic effect |
|---|---|---|---|
| — | Sponsor creates and funds | `funded` | Exact `gl.message.value` recorded in `deposited` |
| `funded` | Named beneficiary accepts while `now < deliver_by` | `active` | Terms unchanged; funds remain held |
| `funded` | Sponsor cancels | `refund_dispatched` | Full ledger debited, sponsor transfer emitted |
| `funded` / `active` | `now >= deliver_by` without submission | `refund_dispatched` | Full ledger debited, sponsor transfer emitted |
| `active` | Beneficiary submits once while `now < deliver_by`; URL policy passes | `submitted` | Artifact/evidence commitments fixed; review deadline starts |
| `submitted` / `retryable` | Validators agree on exact affirmative approval | `approved` | Funds remain locked until `settle` |
| `submitted` / `retryable` | Substantive semantic rejection | `blocked` | Full sponsor refund becomes settleable |
| `submitted` / `retryable` | Deterministic integrity failure | `blocked` | Full sponsor refund becomes settleable |
| `submitted` / `retryable` | Valid analysis is semantically uncertain, attempts 1–2 | `retryable` | Funds stay locked; cooldown applies |
| `retryable` | Third valid semantic uncertainty result | `blocked` | Full sponsor refund becomes settleable |
| `submitted` / `retryable` | Infrastructure/format/consensus failure | `retryable` | Funds stay locked; cooldown applies; review remains available until deadline |
| `submitted` / `retryable` | `now >= review_deadline` | `refund_dispatched` | Permissionless full sponsor refund; no web/LLM call |
| `approved` | Anyone calls `settle` once | `payout_dispatched` | Full ledger debited, beneficiary transfer emitted |
| `blocked` | Anyone calls `settle` once | `refund_dispatched` | Full ledger debited, sponsor transfer emitted |

Reviews and submissions lose at exact deadline equality; expiry wins at
`now >= deadline`. Acceptance and submission require strict `now < deliver_by`.
The review deadline is fixed at submission from the creation-time review
window. There is no Counta `inconclusive`, split-payout, or economic
`UNDETERMINED` state.

## Economic invariant and transfer accounting

For original deposit `D`, a terminal dispatch records exactly one recipient:

| Finalized Counta adjudication | Sponsor amount | Beneficiary amount |
|---|---:|---:|
| Approved | 0 | `D` |
| Semantic rejection | `D` | 0 |
| Deterministic integrity failure | `D` | 0 |
| Third valid semantic uncertainty | `D` | 0 |
| Pre-acceptance cancellation | `D` | 0 |
| Delivery/review deadline expiry | `D` | 0 |

There is no partial outcome. Before `_send_gen`, settlement records the
recipient-specific and total dispatched amounts, zeros `deposited`, writes the
terminal status and settlement reason, then emits the single transfer. This
checks-effects-interactions ordering and terminal status prevent a second
dispatch. Accounting requires `sponsor_dispatched_amount +
beneficiary_dispatched_amount == dispatched_amount`, exactly one side to equal
the full dispatch, and `deposited == 0` after terminal dispatch.

The transfer is a GenLayer child transfer. The parent status
`payout_dispatched`/`refund_dispatched` means the contract emitted the transfer
instruction; it does not synchronously prove final credit. Integrators must
follow the child transaction and check its final result and `value_credited`
when exposed. Protocol-level child-transfer failure does not restore the
Counta ledger automatically.

## Review budgets and infrastructure policy

Only sponsor or beneficiary may trigger a review; outsiders cannot burn either
budget. A retryable result sets a 15-minute cooldown. Semantic and
infrastructure counters are independent. Semantic uncertainty means a valid,
hash-verified structured analysis whose decision is neither blocked nor
approved. Two such results remain retryable; the third deterministically blocks
with sponsor refund eligibility (`semantic_uncertainty_sponsor_refund`).

Infrastructure includes HTTP 408, 429, 5xx, network exceptions, malformed HTTP
status metadata, LLM execution failure, malformed structured output, invalid
consensus returns and observation failures. They increment a telemetry counter
capped at three, but that counter is never authorization-critical and never
blocks another review.
Every infrastructure failure remains `retryable`, stores its reason, and sets
`next_review_at=now + 900 seconds`. Either party may retry after cooldown while
`now < review_deadline`, even after ten or more failures. These failures remain
non-authorizing, do not change semantic attempts, and do not enable settlement.
After provider recovery, a valid later review can still approve before the
deadline. `settle()` remains unavailable while retryable; only permissionless
`expire()` at `now >= review_deadline` refunds unresolved funds. Retries never
extend the fixed deadline. At exact equality, review is rejected and expiry is
allowed.

Deterministic artifact-integrity failures (non-retryable HTTP response, empty
or oversized content, invalid response body, hash mismatch, invalid UTF-8 or
unsupported image bytes) become `blocked`. HTTP 408/429/5xx and fetch/network
exceptions remain retryable infrastructure failures. HTTP 404 and other
non-success statuses not explicitly retryable are deterministic submission
integrity failures under this policy.

## Artifact verification and prompt trust boundary

Before entering `run_nondet_unsafe`, review copies persistent values into a
deterministic in-memory snapshot, including the brief, URLs, approved host,
hashes, summary and artifact kind. Each leader and validator independently:

1. fetches raw bytes;
2. enforces bounded size and success status;
3. hashes the exact raw bytes with SHA-256 and checks the stored commitment;
4. decodes UTF-8 only after digest verification for text/evidence, or checks a
   PNG/JPEG signature and attaches the verified raw image bytes;
5. semantically reviews only after all deterministic integrity checks pass.

All user-controlled text and provenance metadata are encoded into one canonical,
sorted JSON object between explicit untrusted-data markers. This contains the
brief, summary, evidence, evidence/deliverable URLs and hostnames, immutable
approved hostname, artifact kind, and committed text deliverable. Instructions
inside any of these fields are data. For images, visible words are explicitly
untrusted evidence, never reviewer commands. This framing reduces prompt
confusion; it cannot mathematically eliminate model susceptibility.

The model returns exactly the decision fields `deliverable_match`,
`evidence_support`, `risk`, `confidence`, and `rationale`. Approval requires the
exact tuple `yes / yes / no` and integer confidence at least 75. Missing or
invalid confidence becomes zero; invalid enums or malformed JSON become
infrastructure errors, never approval. Unknown extra fields are rejected.
Rationale is bounded informational text, never an authorization input.

## Validator equivalence and protocol consensus

The leader and validators independently run the complete artifact fetch,
integrity, and semantic pipeline. Equivalence groups only results with the
same deterministic class: analysis outcomes compare `approved`, `blocked`, or
`retryable`; infrastructure error subclasses may compare because all consume
only the infrastructure budget and cannot settle; integrity failure compares
only with integrity failure. Analysis, infrastructure error, and integrity
failure are never interchangeable.

For an `approved` equivalence result, each analysis independently satisfies
the full exact safe tuple and threshold. Thus confidence 80 and 97 can agree on
authorization, but 74 is retryable and cannot validate the 80 approval. For
blocked and retryable outcomes, diagnostic field, rationale, and confidence
differences do not change the deterministic economic outcome. A blocked reason
variance is safe because all such outcomes refund the sponsor; a retryable
variance remains non-authorizing and non-settleable. GenLayer protocol
`Undetermined`, timeouts, or validator disagreement are not Counta decisions:
they do not authorize a status transition, so clients must inspect canonical
state before retries or settlement.

## URL and storage limitations

URLs require HTTPS, allow only port 443, reject credentials and fragments, and
reject every IP literal, including public addresses, IPv4-mapped IPv6, private,
loopback, link-local, multicast, unspecified, reserved, and shared CGNAT
addresses such as `100.64.0.0/10`. DNS hostnames require at least two labels;
single-label names such as `metadata` and `internal` are rejected. These syntax
checks cannot establish public DNS resolution, prevent DNS rebinding, or inspect
the complete redirect chain if the platform follows redirects. Immutable URLs
and integration-level public-host checks are recommended. Distinct CDN
hostnames are not proof of independence.

There is no lifetime milestone cap. Persistent milestone records are retained;
party-local aliases are also retained so parties can use an unambiguous local
ID conveniently. Sponsor aliases exist at creation; beneficiary aliases are
created only on acceptance. Alias conflicts are marked ambiguous rather than
redirected; the composite reference always identifies the intended record.
Storage growth and chain-level capacity/cost remain practical limits. No
cleanup/delete path can erase historical accounting.
