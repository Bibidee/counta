# Counta protocol design (v0.3.3, current deployed release)

Counta holds sponsor-provided GEN against one fixed milestone. The sponsor
commits the parties, brief, delivery deadline, review window and exact allowed
evidence hostname before beneficiary acceptance. A single hash-bound submission
is independently fetched and semantically assessed through GenLayer. Only
deterministic state logic releases funds.

v0.3.3 is deployed to GenLayer Studionet (chain ID 61999) at
`0xC3402F827Ba8E6ee706A8290B4a47d2b447285B2`. Deployment transaction:
`0x5627121e05f5e0ccfed6071b978049dd2b215023dafbbef91894fce1ed5b15a7`;
deployment finalized with MAJORITY_AGREE and GenVM SUCCESS. Frozen source
commit and tag: `7fa406e9f5d712c237d241c6a5daedf04b2b5909` / `v0.3.3`;
SHA-256 `c1160498a29145ac2806a555ec5121d5e858a16d384ec5184b11f9cb68272ff6`;
Git blob `85646a19c6171e6503b47151b902917c0b7cf4b1`; source length 38,570
bytes. The official GenLayer CLI retrieved deployed source and the raw bytes
matched the frozen source exactly. The release gate passed 132 tests with no
skips or failures; preflight, GenVM lint, ABI/schema, and exact-source GitHub
Actions run `37456630767` passed. Full `get_info()` and live receipts are in
`docs/DEPLOYMENT.md`.

Live v0.3.3 evidence includes an approved 0.001 GEN beneficiary payout, an
explicit semantic block/refund with credited sponsor transfer, and a genuine
evidence 404 that remained retryable until the exact committed bytes were
published; the beneficiary then reviewed during the sponsor's active
cooldown. Fixtures are repository-owned and do not establish independent
authorship or real-world truth.

v0.3.2 is historical and superseded at
`0x5E7D5C3039713b50aD46d09C3c1ad0c7194ce07e`; deployment transaction
`0xca44755d4d4166f238d3a5243e66c721d5870c3f2180b294a21b42d905fe0c12`;
source commit `e546d8b83c67adb67fd0780961e1159822b14980`; SHA-256
`ae899a586ee77a316870a800aa8c4baf9c12d7f8267320d14691327dc551f1ac`;
36,598 bytes; source parity verified. Its live payout and refund records
remain in `docs/DEPLOYMENT.md` and are not v0.3.3 evidence.

v0.3.1 is a historical, superseded deployment at
`0xE4Bb7FC4C217EE867F14d40aFaa1e868693CDcAB`. Its frozen source commit is
`8c7d472522e90b481bce56794c175e2e951c99fa`; contract SHA-256:
`9b98e0016a38e7c4ad8e613370b0667e7c4b37910e4dbaf26e99a6a1688be005`;
source length: 36,535 bytes. Its source parity was verified byte-for-byte.
v0.3.0 remains historical and superseded at
`0x4235915E7ec84596239b2d29B93d1a2A982A1018`; its approval/payout evidence is
preserved in `docs/DEPLOYMENT.md`. v0.3.2 removed the terminal
semantic-uncertainty retry budget, classifies HTTP 403 as transient
infrastructure, and excludes colons from local milestone IDs.

## Identity and evidence authority

The sponsor-local ID is not globally unique. Counta stores each record under a
canonical reference derived from the normalized sponsor address and local ID:

```text
0x<sponsor-address-lowercase>:<sponsor-local-id>
```

`create_milestone` returns that canonical reference. Subsequent methods accept
it, so integrations never need to guess which sponsor namespace a local name
means. Local IDs match `[A-Za-z0-9][A-Za-z0-9_.-]{0,95}`; colon is forbidden
because it delimits canonical references. The sponsor alias is registered at creation. A beneficiary alias is
registered only when the named beneficiary accepts; until then the beneficiary
must use the canonical reference. If an accepted party-local alias collides,
that alias becomes ambiguous and callers must use the composite reference.
This prevents an unrelated sponsor from poisoning a wallet's alias merely by
nominating that wallet as beneficiary. The scoped storage key prevents
unrelated wallets from reserving another sponsor's ID. Historical records are
not deleted. The local-ID grammar makes the canonical-reference delimiter
unambiguous. Integrations should store and use the canonical `milestone_ref`
returned by `create_milestone`.

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
| `submitted` / `retryable` | Deterministic deliverable integrity failure | `blocked` | Full sponsor refund becomes settleable |
| `submitted` / `retryable` | Evidence retrieval, hash, decode, empty, or size failure | `retryable` | Sponsor-selected evidence-source failure cannot create an early refund |
| `submitted` / `retryable` | Valid analysis is semantically uncertain | `retryable` | Funds stay locked; cooldown applies; uncertainty never creates a terminal refund |
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

Only sponsor or beneficiary may trigger a review. Retry cooldowns are
party-specific: a sponsor's retry sets only `sponsor_next_review_at`, and a
beneficiary's retry sets only `beneficiary_next_review_at`, each to
`now + 900 seconds`. The opposite party may still review immediately. Each
party remains independently rate-limited. Cooldowns never extend the fixed
review deadline. Semantic uncertainty is a valid hash-verified analysis whose
decision is neither approved nor explicitly rejected. It remains `retryable`;
neither bounded telemetry counter can block review, enable settlement, or
refund funds. If the state remains `submitted` or `retryable` at the deadline,
permissionless `expire()` refunds the sponsor.

Infrastructure includes network exceptions, malformed HTTP status/body,
LLM execution failure, malformed structured output, invalid consensus returns,
and observation failures. Infrastructure attempts are telemetry capped at
three, not a retry budget. Every such failure remains `retryable`, and only the
initiating party's cooldown is set. Failed observations cannot settle or refund
escrow. At exact review-deadline equality, review is rejected and expiry is
allowed.

The artifact roles have intentionally different failure policies. The
beneficiary commits the deliverable bytes; the sponsor selects the evidence
authority. A permanent defect in the beneficiary's deliverable commitment may
therefore block, but an evidence server controlled or influenced by the sponsor
must not be able to manufacture an immediate sponsor-favorable refund.

| Deliverable response/content | Result |
|---|---|
| HTTP 200 with exact non-empty bounded bytes, valid text UTF-8 or supported PNG/JPEG | Continue to verified semantic review |
| HTTP 403, 408, 429, 5xx, network exception, malformed status/body, or surfaced 3xx redirect | `retryable` |
| HTTP 404/410 or another non-special non-2xx response | `blocked` |
| Hash mismatch, empty/oversized bytes, invalid UTF-8, or unsupported image bytes | `blocked` |

| Evidence response/content | Result |
|---|---|
| HTTP 200 with exact non-empty bounded UTF-8 bytes and matching SHA-256 | Continue to verified semantic review |
| HTTP 403/404/408/410/429/5xx, any other non-2xx, network exception, malformed status/body, or surfaced 3xx | `retryable` as `evidence_unavailable` |
| Hash mismatch, empty/oversized bytes, or invalid UTF-8 | `retryable` as `evidence_unavailable` |

Evidence failures never become semantic rejection: the model is called only
after the exact evidence bytes have been fetched, bounded, hash-verified, and
decoded. Only then can substantive `evidence_support` or `risk` analysis block.

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
checks cannot establish public DNS resolution or prevent DNS rebinding. The
supported `gl.nondet.web.get(url)` surface and its documented response expose
status/body, but no final URL, redirect history, resolved IP, or redirect-disable
parameter; Counta cannot enforce the origin after a redirect if the runtime
follows one. Counta guarantees only that the submitted evidence URL hostname
matches the sponsor-approved hostname lexically. Immutable URLs and
integration-level public-host checks are recommended. Distinct CDN hostnames
are not proof of independence.

There is no lifetime milestone cap. Persistent milestone records are retained;
party-local aliases are also retained so parties can use an unambiguous local
ID conveniently. Sponsor aliases exist at creation; beneficiary aliases are
created only on acceptance. Alias conflicts are marked ambiguous rather than
redirected; the composite reference always identifies the intended record.
Storage growth and chain-level capacity/cost remain practical limits. No
cleanup/delete path can erase historical accounting.
