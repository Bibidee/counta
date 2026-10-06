# Counta

Counta is a standalone GenLayer Intelligent Contract primitive for milestone
evidence escrow. A sponsor fixes the beneficiary, brief, amount, deadlines, and
one exact evidence-authority hostname before the beneficiary accepts. The
beneficiary submits one text or image deliverable and text evidence, both bound
to SHA-256 hashes. Validators independently retrieve and verify those exact
bytes, then semantically assess the submission. Deterministic contract logic
alone decides whether the complete escrow is dispatched to the beneficiary or
refunded to the sponsor.

Counta is an escrow primitive, not a frontend, marketplace, identity provider,
or guarantee that work is truthful or legally compliant.

## Why GenLayer?

Ordinary deterministic contract code cannot reliably judge whether a photograph,
document, or other unstructured deliverable satisfies a natural-language brief.
Counta uses GenLayer's independent validator execution to fetch the committed
artifacts and perform that bounded semantic judgment. A single off-chain model
or centralized verifier could selectively approve evidence; Counta instead
requires validators to independently retrieve the exact hash-bound materials
and agree on the authorization outcome. No one model's rationale authorizes
payment. This still cannot eliminate model fallibility, provider outages,
validator disagreement, or protocol-level `UNDETERMINED` outcomes.

## v0.3.3 hardening

- Sponsor-fixed evidence authority: creation commits one normalized DNS
  hostname. Beneficiaries may submit evidence only from that exact hostname;
  no wildcards or subdomain matching are used.
- Sponsor-scoped milestone identity: local IDs use only ASCII letters, digits,
  underscore, dot, and hyphen after an alphanumeric first character; colon is
  forbidden so a local ID cannot impersonate a canonical reference. The
  returned canonical reference is `0x<sponsor-address>:<local-id>`. Party-local
  convenience lookup is sponsor-side at creation and beneficiary-side only
  after acceptance; use the canonical reference for first acceptance and shared
  IDs. Colliding aliases are ambiguous, but canonical references remain unique.
- Strict payment rule: affirmative approval dispatches 100% of the escrow to
  the beneficiary. Explicit semantic rejection or deterministic artifact
  integrity failure dispatches 100% to the sponsor. Semantic uncertainty never
  becomes a terminal result merely because it repeats; unresolved work becomes
  refundable only at the fixed review deadline through permissionless `expire()`.
  No split or Counta-level inconclusive state exists.
- Evidence and deliverables have separate failure economics. Every sponsor-
  selected evidence-source retrieval/content failure (including HTTP errors,
  redirects, wrong bytes, empty/oversized content, and invalid UTF-8) is
  `retryable`; semantic support is judged only after exact evidence bytes are
  fetched and verified. This prevents the sponsor's evidence source from
  creating an early sponsor-favorable refund. Deterministic deliverable
  integrity failures remain `blocked`; transient deliverable fetch failures
  are `retryable`.
- Sponsor and beneficiary have independent 15-minute review cooldowns. A
  retry by one party never consumes the other's review opportunity. Neither
  cooldown extends the fixed review deadline. The semantic and infrastructure
  counters remain bounded telemetry only; unresolved funds become refundable
  only through permissionless `expire()` at the deadline.
- Deliverable HTTP 403/408/429/5xx and surfaced redirects are retryable;
  other surfaced non-2xx responses and deterministic content failures block.
  Every evidence HTTP/source/content/hash failure is retryable. Network/LLM
  errors, malformed output, and failed consensus never approve.
- Prompt inputs are one canonical JSON data block. Brief, summary, evidence,
  URLs, text deliverable, and visible image words are all untrusted content, not
  reviewer instructions. Image evidence is raw PNG/JPEG input; the evaluator is
  told not to treat visible words as instructions.
- Raw response bytes are checked against SHA-256 before decoding. The digest
  binds bytes, not authorship, truth, DNS ownership, or correctness.
- Validator equivalence compares the deterministic economic outcome. Each
  validator must independently pass the exact approval tuple and confidence
  threshold for an approval; rationale and confidence values need not match.
  Integrity failures cannot be equivalent to infrastructure errors.
- Terminal names are `payout_dispatched` and `refund_dispatched`: Counta records
  a transfer dispatch, not proof of child-transfer credit. Integrators must
  inspect the child receipt and `value_credited` where exposed.

## Lifecycle

1. Sponsor funds `create_milestone(local_id, beneficiary, brief,
   approved_evidence_host, deliver_by, review_window)`. It returns the canonical
   sponsor-scoped `milestone_ref`.
2. The named beneficiary accepts before the fixed delivery deadline using the
   sponsor-returned canonical reference; a beneficiary convenience alias is
   registered only after that acceptance.
3. That beneficiary submits exactly once, before `deliver_by`, with a committed
   text/image URL and hash, evidence URL and hash, and bounded summary. The
   evidence hostname must exactly equal the sponsor's creation-time policy.
4. Sponsor or beneficiary can trigger review. Retry cooldown is deterministic;
   semantic and infrastructure counters are bounded telemetry, not shared
   authorization or refund budgets.
5. An affirmative consensus result allows permissionless one-time settlement
   to dispatch the entire ledger to the beneficiary. Explicit semantic or
   integrity rejection permits a full sponsor refund. Uncertainty and
   infrastructure failures remain retryable after cooldown until
   fixed-deadline expiry refunds unresolved funds.

## Trust and platform boundaries

- HTTPS syntax checks reject credentials, fragments, unsupported ports, local
  names, every IP literal (including public and CGNAT ranges), and single-label
  DNS names. The submitted evidence URL's lexical hostname must exactly match
  the sponsor-approved hostname. The documented GenLayer web response exposes
  response status/body but no redirect chain/final URL or redirect-disable
  option; Counta therefore cannot prove the final redirect origin or prevent
  DNS rebinding through lexical checks alone.
- A hostname selected by a sponsor expresses the sponsor's evidence-authority
  policy, not proof of independent authorship. Distinct hostnames/CDNs are not
  proof of independent sources.
- `UNDETERMINED` and other protocol outcomes are not Counta verdicts and never
  authorize payment. Integrators must read canonical milestone state before
  acting and obey deadlines/cooldowns.
- Milestone history is retained. There is no lifetime cap, but practical usage
  remains subject to chain storage capacity and costs.
- A `*_dispatched` state does not prove that the child transfer credited the
  recipient. Follow the child receipt to finality and verify `value_credited`.

## Release status

**Current deployed release: v0.3.3.** The Studionet contract is
[`0xC3402F827Ba8E6ee706A8290B4a47d2b447285B2`](https://explorer-studio.genlayer.com/address/0xC3402F827Ba8E6ee706A8290B4a47d2b447285B2).
Deployment transaction:
[`0x5627121e05f5e0ccfed6071b978049dd2b215023dafbbef91894fce1ed5b15a7`](https://explorer-studio.genlayer.com/tx/0x5627121e05f5e0ccfed6071b978049dd2b215023dafbbef91894fce1ed5b15a7),
FINALIZED / MAJORITY_AGREE / GenVM SUCCESS. Frozen source commit and tag:
`7fa406e9f5d712c237d241c6a5daedf04b2b5909` / `v0.3.3`; contract SHA-256
`c1160498a29145ac2806a555ec5121d5e858a16d384ec5184b11f9cb68272ff6`, Git
blob `85646a19c6171e6503b47151b902917c0b7cf4b1`, 38,570 bytes. Official CLI
source retrieval and byte comparison confirmed exact deployed-source parity.
Exact `get_info()`, CI, and all live lifecycle receipts are recorded in
[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).

The frozen-source release gate passed 132 tests, 0 failed, 0 skipped;
preflight, GenVM lint, and ABI/schema passed. Exact-source GitHub Actions
[37456630767](https://github.com/Bibidee/counta/actions/runs/37456630767)
completed successfully. The live v0.3.3 evidence includes: an approved payout
with `value_credited=true`; a genuine semantic rejection and credited sponsor
refund; and a controlled evidence-source 404 that remained retryable, followed
by publishing the exact committed bytes and approval from the beneficiary
while the sponsor cooldown was still active. All fixtures are repository-
owned, so these demonstrate contract behavior and exact-byte handling, not
independent authorship or real-world truth. Final documentation-head CI is
recorded in `docs/DEPLOYMENT.md` after it completes.

**Historical deployed release: v0.3.2 (superseded).** Address
[`0x5E7D5C3039713b50aD46d09C3c1ad0c7194ce07e`](https://explorer-studio.genlayer.com/address/0x5E7D5C3039713b50aD46d09C3c1ad0c7194ce07e);
deployment transaction
[`0xca44755d4d4166f238d3a5243e66c721d5870c3f2180b294a21b42d905fe0c12`](https://explorer-studio.genlayer.com/tx/0xca44755d4d4166f238d3a5243e66c721d5870c3f2180b294a21b42d905fe0c12);
source commit `e546d8b83c67adb67fd0780961e1159822b14980`; SHA-256
`ae899a586ee77a316870a800aa8c4baf9c12d7f8267320d14691327dc551f1ac`;
36,598 bytes, parity verified. Its historical source-head CI run
[37430349521](https://github.com/Bibidee/counta/actions/runs/37430349521)
passed with 105 tests. Its approved payout and blocked/refund evidence remain
fully preserved in the deployment record.

**Historical deployed release: v0.3.1 (superseded).** The Studionet contract is
[`0xE4Bb7FC4C217EE867F14d40aFaa1e868693CDcAB`](https://explorer-studio.genlayer.com/address/0xE4Bb7FC4C217EE867F14d40aFaa1e868693CDcAB).
Deployment transaction:
[`0xa8b3ed6c3e0a6b297d5017350c7cef3b46f05fb0b3eb9ae8343a10b7d31ddced`](https://explorer-studio.genlayer.com/tx/0xa8b3ed6c3e0a6b297d5017350c7cef3b46f05fb0b3eb9ae8343a10b7d31ddced),
FINALIZED / MAJORITY_AGREE / GenVM SUCCESS. The deployed source was retrieved
through `gen_getContractCode` and verified byte-for-byte against frozen
commit `8c7d472522e90b481bce56794c175e2e951c99fa`; both sources are 36,535
bytes with SHA-256
`9b98e0016a38e7c4ad8e613370b0667e7c4b37910e4dbaf26e99a6a1688be005`.
`get_info()` reports Counta 0.3.1. A fresh live v0.3.1 flow finalized as
`funded -> active -> submitted -> blocked -> refund_dispatched`; it did not
produce a beneficiary payout. A second v0.3.1 release-attestation flow
finalized `funded -> active -> submitted -> approved -> payout_dispatched`;
the child transfer finalized with `value_credited=true` for the designated
beneficiary. These historical v0.3.1 outcomes, including exact transactions and
artifact commitments, are recorded in [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).

**Historical deployed release: v0.3.0 (superseded).** It is deployed to Studionet at
[`0x4235915E7ec84596239b2d29B93d1a2A982A1018`](https://explorer-studio.genlayer.com/address/0x4235915E7ec84596239b2d29B93d1a2A982A1018).
The deployment is `FINALIZED / MAJORITY_AGREE / GenVM SUCCESS`; retrieved
deployed source matches the frozen local contract byte-for-byte. A real live
milestone completed `funded -> active -> submitted -> approved ->
payout_dispatched`, and its child transfer receipt reports `value_credited=true`.
The live artifacts are repository-owned fixtures on two hostnames, not
independently authored evidence. Full hashes, transaction links, CI, and
deployment provenance are in [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).

The earlier v0.2.0 deployment at
[`0x8E1C18c660bf14d684ea5C1827D8d99BE27442f7`](https://explorer-studio.genlayer.com/address/0x8E1C18c660bf14d684ea5C1827D8d99BE27442f7)
is historical and superseded; it does not contain v0.3.0 changes.

## Build and test

Use Python 3.12 and the exact constraints lock:

```powershell
python -m pip install -r requirements.txt -c requirements-lock.txt
python -m pytest tests/direct -q
python scripts/preflight.py
```

Preflight verifies the single deployable source, syntax/compilation, GenVM lint,
generated ABI byte equality, and the complete Direct Mode suite. CI runs this
same gate on Ubuntu using the unmodified stock Direct Mode loader; the test-only
stdin workaround is limited to Windows.

## Release acceptance checklist

For a future contract release, require a clean frozen commit and passing tests,
preflight, lint, schema, and GitHub Actions on that exact commit. Record the
contract SHA-256, deploy only those exact bytes, retrieve and byte-compare the
deployed source, verify `get_info()`, and inspect child transfer receipts and
`value_credited` rather than inferring payment from a dispatch state. v0.3.0's
historical verified deployment evidence remains in
[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).
