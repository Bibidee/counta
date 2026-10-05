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

## v0.3.1 candidate policy

- Sponsor-fixed evidence authority: creation commits one normalized DNS
  hostname. Beneficiaries may submit evidence only from that exact hostname;
  no wildcards or subdomain matching are used.
- Sponsor-scoped milestone identity: the local ID is unique per sponsor. The
  returned canonical reference is `0x<sponsor-address>:<local-id>`. Party-local
  convenience lookup is sponsor-side at creation and beneficiary-side only
  after acceptance; use the canonical reference for first acceptance and shared
  IDs. Colliding aliases are ambiguous, but canonical references remain unique.
- Strict payment rule: affirmative approval dispatches 100% of the escrow to
  the beneficiary. Semantic rejection, deterministic artifact-integrity failure,
  and exhausted semantic uncertainty dispatch 100% to the sponsor. No split or
  Counta-level inconclusive state exists.
- Infrastructure failures—including 408, 429, 5xx, network/LLM errors, malformed
  model output, and failed consensus returns—never approve and never make funds
  immediately refundable. Each failure sets the ordinary retry cooldown; the
  infrastructure counter is telemetry capped at three and never blocks another
  review. Either party may retry after cooldown until the fixed review deadline,
  when permissionless `expire()` refunds unresolved funds to the sponsor.
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
4. Sponsor or beneficiary can trigger review. Retry cooldown and semantic and
   infrastructure attempt counters are deterministic and independent.
5. An affirmative consensus result allows permissionless one-time settlement
   to dispatch the entire ledger to the beneficiary. A semantic/integrity block
   permits full sponsor refund. Infrastructure failures remain retryable after
   cooldown until fixed-deadline expiry refunds unresolved funds.

## Trust and platform boundaries

- HTTPS syntax checks reject credentials, fragments, unsupported ports, local
  names, every IP literal (including public and CGNAT ranges), and single-label
  DNS names. Static checks cannot guarantee DNS answers or redirect behavior;
  GenLayer's web response does not expose a redirect chain/final URL or a
  redirect-disable control.
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

**Current release candidate: v0.3.1 — NOT DEPLOYED.** It removes an
infrastructure-retry lockout and hardens URL and alias admission. It has no
address, deployment transaction, or live v0.3.1 lifecycle evidence yet. Its
local candidate source SHA-256 is
`9b98e0016a38e7c4ad8e613370b0667e7c4b37910e4dbaf26e99a6a1688be005` (36,535
bytes).

**Historical deployed release: v0.3.0.** It is deployed to Studionet at
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

Before deploying v0.3.1, require a clean frozen commit and passing tests,
preflight, lint, schema, and GitHub Actions on that exact commit. Record the
contract SHA-256, deploy only those exact bytes, retrieve and byte-compare the
deployed source, verify `get_info()`, and inspect child transfer receipts and
`value_credited` rather than inferring payment from a dispatch state. v0.3.0's
historical verified deployment evidence remains in
[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).
