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

## v0.3.0 candidate policy

- Sponsor-fixed evidence authority: creation commits one normalized DNS
  hostname. Beneficiaries may submit evidence only from that exact hostname;
  no wildcards or subdomain matching are used.
- Sponsor-scoped milestone identity: the local ID is unique per sponsor. The
  returned canonical reference is `0x<sponsor-address>:<local-id>`. Party-local
  convenience lookup works only where unambiguous; use the composite reference
  for integrations and shared IDs.
- Strict payment rule: affirmative approval dispatches 100% of the escrow to
  the beneficiary. Semantic rejection, deterministic artifact-integrity failure,
  and exhausted semantic uncertainty dispatch 100% to the sponsor. No split or
  Counta-level inconclusive state exists.
- Infrastructure failures—including 408, 429, 5xx, network/LLM errors, malformed
  model output, and failed consensus returns—never approve and never make funds
  immediately refundable. Three finalized failures stop further review attempts;
  the escrow stays locked until permissionless `expire()` at the fixed review
  deadline, then the full balance is returned to the sponsor.
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
2. The named beneficiary accepts before the fixed delivery deadline.
3. That beneficiary submits exactly once, before `deliver_by`, with a committed
   text/image URL and hash, evidence URL and hash, and bounded summary. The
   evidence hostname must exactly equal the sponsor's creation-time policy.
4. Sponsor or beneficiary can trigger review. Retry cooldown and semantic and
   infrastructure attempt counters are deterministic and independent.
5. An affirmative consensus result allows permissionless one-time settlement
   to dispatch the entire ledger to the beneficiary. A semantic/integrity block
   permits full sponsor refund. Infrastructure exhaustion does not settle;
   only fixed-deadline expiry refunds it.

## Trust and platform boundaries

- HTTPS syntax checks reject credentials, fragments, unsupported ports, local
  names and non-public IP literals. Static checks cannot guarantee DNS answers
  or redirect behavior; GenLayer's web response does not expose a redirect
  chain/final URL or a redirect-disable control.
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

**v0.3.0 is a pre-deployment candidate and is not deployed.** The Studionet
deployment at
[`0x8E1C18c660bf14d684ea5C1827D8d99BE27442f7`](https://explorer-studio.genlayer.com/address/0x8E1C18c660bf14d684ea5C1827D8d99BE27442f7)
is historical v0.2.0 only and does not contain the v0.3.0 changes. Its exact
source, deployment, and live lifecycle evidence remain in
[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md). Do not use it as v0.3.0 parity or
deployment evidence.

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

Before freezing or deploying v0.3.0: clean tree; all tests/preflight/lint/schema
pass; GitHub Actions succeeds on the exact release commit; record the source
SHA-256 and tag the frozen release; deploy only that tagged source; retrieve and
byte-compare deployed source; verify `get_info()`; run real approval and refund
lifecycle evidence; and verify each child transfer receipt and `value_credited`.
This repository currently records no v0.3.0 deployment or live lifecycle.
