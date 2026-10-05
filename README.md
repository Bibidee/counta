# Counta

**Counta is a standalone GenLayer Intelligent Contract for milestone evidence
escrow.** A sponsor locks native GEN against a fixed brief and a named
beneficiary. The beneficiary submits one text or image deliverable with
hash-bound supporting evidence. GenLayer validators independently fetch the
exact committed artifacts and judge whether the work satisfies the brief.
Deterministic contract logic controls retries, deadlines, and one-time
settlement.

Counta is an escrow primitive, not a frontend, marketplace, identity service,
or guarantee that work is truthful or legally compliant.

## Why GenLayer?

Ordinary contract code cannot reliably decide whether an unstructured file,
photo, or evidence document substantively satisfies a natural-language
milestone brief. Counta uses GenLayer's nondeterministic execution for that
bounded semantic assessment while keeping custody accounting, access rules,
deadline checks, and payouts deterministic. No single off-chain service is
trusted to write the outcome: the result is subject to GenLayer validator
consensus. Consensus can still disagree or fail to finalize; Counta does not
promise to eliminate `UNDETERMINED` outcomes.

## Lifecycle

1. **Fund:** sponsor calls payable `create_milestone`; only `gl.message.value`
   is credited to the stored escrow ledger.
2. **Submit:** the designated beneficiary submits once before the fixed
   deadline, committing deliverable/evidence HTTPS URLs and SHA-256 hashes.
3. **Review:** validators fetch raw bytes, verify hashes programmatically, then
   assess the exact text or raw image plus evidence against the immutable brief.
4. **Settle:** any account may trigger the deterministic payout after a
   finalized decision: approved pays beneficiary; blocked refunds sponsor;
   inconclusive or review timeout splits 50/50 (odd wei to beneficiary).
5. **Recover:** sponsor may cancel before submission; anyone may refund an
   unsubmitted milestone after its delivery deadline. Every route zeroes the
   ledger before transfer and is one-time.

| Result | Settlement |
|---|---|
| `approved` | Entire escrow to beneficiary |
| `blocked` | Entire escrow back to sponsor |
| `inconclusive` / review timeout | 50/50 sponsor/beneficiary split |
| Unsubmitted delivery deadline / pre-submit cancellation | Entire escrow back to sponsor |

Three finalized retryable reviews (for example, unavailable sources, malformed
model output, or low-confidence/unclear assessment) produce `inconclusive` so a
public deterministic split is available. Consensus-level disagreement may
prevent a review transaction from finalizing; if the review window later
expires, the same timeout split applies.

## Artifact and image commitments

Counta computes SHA-256 on the exact raw HTTP response bytes before any UTF-8
decoding. Text deliverables and textual evidence must decode as UTF-8. Image
deliverables support raw PNG/JPEG bytes passed to `gl.nondet.exec_prompt` via
its documented `images` argument; images are capped at 2 MB. Evidence is UTF-8
text capped at 16 KB. Prompt instructions treat brief, summary, artifacts, and
evidence as untrusted data. Hash mismatch, unsupported image, empty artifact,
bad HTTP response, or invalid UTF-8 cannot approve. Transient network/provider
failures remain non-approving and retryable.

## Security model and tradeoffs

- Exact SHA-256 bindings prevent silent replacement between commitment and
  review; a hash does not prove authorship or truth.
- HTTPS validation rejects localhost, `.local`, non-public IP literals,
  non-443 ports, credentials, fragments, and malformed hosts. It cannot prove
  DNS answers or redirect safety in every validator environment.
- Approval requires the same exact semantic outcome and safety fields across
  validators, with confidence within 20 points. Rationale wording is not
  consensus-critical. Approval requires `deliverable_match=yes`,
  `evidence_support=yes`, `risk=no`, and confidence >= 75.
- Uncertainty is not approval. Explicit semantic rejection is blocked; unclear
  assessments or provider/source problems are retryable, then inconclusive.
- An inconclusive milestone splits principal evenly. This bounded risk-sharing
  rule must be understood by both parties before funding.
- There is no challenge/appeal phase after review in v0.1.0.
- Records are bounded to 256 lifetime milestones and cannot be deleted.
- Native GEN is sent using GenLayer external value-transfer messages. Verify
  finalized transfer/message results in addition to the contract's ledger state.

## Build and test

Prerequisite: Python 3.12.

```powershell
python -m pip install -r requirements.txt
python -m pytest tests/direct -q
python scripts/preflight.py
```

Preflight also runs GenVM lint and ABI/schema generation. The tests use the
official pinned `genlayer-test` Direct Mode fixtures (`direct_deploy`,
`direct_vm`, test accounts, `mock_web`, and `mock_llm`); they exercise the actual
contract source, not a fake GenLayer module.

## Current release status

- Version: `0.1.0` (pre-deployment candidate)
- Deployable sources: exactly one, `contracts/counta.py`
- Deployment: **not deployed**
- Live GEN transfer / live semantic consensus: **not yet verified**
- Deployment/source parity: **not applicable until deployment**

See [Design](docs/DESIGN.md) and [Deployment](docs/DEPLOYMENT.md). Do not
represent local mocked tests as live network evidence.
