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

- Version: `0.1.0`
- Deployable sources: exactly one, `contracts/counta.py`
- Studionet contract: [`0xF9e67Ff6f8a156a5357Ae8802402E11814B8887b`](https://explorer-studio.genlayer.com/address/0xF9e67Ff6f8a156a5357Ae8802402E11814B8887b)
- Deployment transaction: [`0x70a708646708dc4cc171a49f79eb1dfe6c41e13ff02218fd9e826ae2906d2272`](https://explorer-studio.genlayer.com/tx/0x70a708646708dc4cc171a49f79eb1dfe6c41e13ff02218fd9e826ae2906d2272)
- Deployment: `FINALIZED`, `MAJORITY_AGREE`, GenVM `SUCCESS`
- Source SHA-256: `d27387ed2f3522a37a642639221b840b9b9faf5426e2f0c079cbbf2a3addc4d5`
- Source parity: byte-for-byte verified using `gen_getContractCode` (28,803 bytes)
- `get_info()`: Counta `0.1.0`, minimum deposit `1000000000000000` wei, minimum confidence `75`
- Release checks: 26 Direct Mode tests passed; lint, schema, and preflight passed; [GitHub Actions](https://github.com/Bibidee/counta/actions/runs/37259378417) passed
- Live milestone lifecycle: **verified**; details below

See [Design](docs/DESIGN.md) and [Deployment](docs/DEPLOYMENT.md). Do not
represent local mocked tests as live milestone or payout evidence.

## Live Studionet lifecycle

On 2026-10-05, a real milestone completed on the deployed contract:

| Step | Transaction | Result |
|---|---|---|
| Fund milestone | [0xdf57f8efce5952dd98316e11eee62cab3e772dacbcfa0d6cc39b2e408000b057](https://explorer-studio.genlayer.com/tx/0xdf57f8efce5952dd98316e11eee62cab3e772dacbcfa0d6cc39b2e408000b057) | FINALIZED, MAJORITY_AGREE, GenVM SUCCESS; 0.001 GEN deposited |
| Submit delivery | [0xff822ce404f8489e48aa092b9cbd7642592b0d6341e1bdb854dd6d91dab09f66](https://explorer-studio.genlayer.com/tx/0xff822ce404f8489e48aa092b9cbd7642592b0d6341e1bdb854dd6d91dab09f66) | FINALIZED, MAJORITY_AGREE, GenVM SUCCESS |
| Semantic review | [0xa990532e0dfae5325d506d96664e54bca1209423893c99a98dfca6b80e4aeac7](https://explorer-studio.genlayer.com/tx/0xa990532e0dfae5325d506d96664e54bca1209423893c99a98dfca6b80e4aeac7) | FINALIZED, MAJORITY_AGREE, GenVM SUCCESS; APPROVED, confidence 85 |
| Settle escrow | [0x472a821d53720d485f98ee06372f47d7fac94448aa3cce5af45a249e666b8447](https://explorer-studio.genlayer.com/tx/0x472a821d53720d485f98ee06372f47d7fac94448aa3cce5af45a249e666b8447) | FINALIZED, MAJORITY_AGREE, GenVM SUCCESS; ledger zeroed and full amount assigned to beneficiary |

The live fixture was `COUNTA-LIVE-20261005-001`. Its [deliverable](https://raw.githubusercontent.com/Bibidee/counta/524ab720e10f632a6a038e58f89cefc169f85ae1/evidence/live-deliverable.txt)
was committed as SHA-256 `b2006a039e3ac90264b58902ea6a573fb18f8c4871f0e60af70555287d2eebe9`;
the [verification evidence](https://cdn.jsdelivr.net/gh/Bibidee/counta@524ab720e10f632a6a038e58f89cefc169f85ae1/evidence/live-verification.txt)
was committed as SHA-256 `48d94b3537b97d678e5d6c436ce686f7837140acfbc7aeadb74caabbb39739a4`.
The contract’s final read reports `status=settled`, `settlement=pay_beneficiary`,
`deposited=0`, and `beneficiary_amount=1000000000000000` wei. The emitted transfer
has child transaction [0x395dcd4d47ca6783e336899cc9f28012f77e531a2853dca6c20732a11c928f76](https://explorer-studio.genlayer.com/tx/0x395dcd4d47ca6783e336899cc9f28012f77e531a2853dca6c20732a11c928f76):
its receipt says `FINALIZED`, `NO_MAJORITY`, and `value_credited=true`. The
beneficiary’s observed balance rose from 448.9959 to 448.9969 GEN, matching the
0.001 GEN payout. This unusual child result is recorded rather than hidden.
