import hashlib
import json
from pathlib import Path


CONTRACT = "contracts/counta.py"
TEXT_DELIVERABLE = b"Counta milestone C-001 deliverable is complete."
EVIDENCE = b"Independent verification confirms the C-001 deliverable is complete."
SPONSOR_AMOUNT = 10**18
NOW = "2026-10-01T12:00:00Z"
DELIVER_BY = 1791115200  # 2026-10-04T12:00:00Z
REVIEW_WINDOW = 21600


def digest(raw):
    return "0x" + hashlib.sha256(raw).hexdigest()


def public_ref(sponsor, local_id):
    return "0x" + sponsor.hex().lower() + ":" + local_id


def new_contract(direct_vm, direct_deploy):
    direct_vm.warp(NOW)
    return direct_deploy(CONTRACT)


def fund(contract, direct_vm, sponsor, beneficiary, milestone_id="C-001", approved_host="evidence.example"):
    direct_vm.sender = sponsor
    direct_vm.value = SPONSOR_AMOUNT
    milestone_ref = contract.create_milestone(
        milestone_id,
        beneficiary,
        "Complete and verify the Counta C-001 text deliverable.",
        approved_host,
        DELIVER_BY,
        REVIEW_WINDOW,
    )
    direct_vm.value = 0
    return milestone_ref


def activate(contract, direct_vm, beneficiary, milestone_id="C-001"):
    sponsor = direct_vm.sender
    direct_vm.sender = beneficiary
    contract.accept_milestone(public_ref(sponsor, milestone_id))


def submit(contract, direct_vm, beneficiary, milestone_id="C-001"):
    activate(contract, direct_vm, beneficiary, milestone_id)
    contract.submit_delivery(
        milestone_id,
        "text",
        "https://deliverable.example/c001.txt",
        digest(TEXT_DELIVERABLE),
        "https://evidence.example/c001.txt",
        digest(EVIDENCE),
        "The committed deliverable and independent completion record are provided.",
    )


def mock_uncertain(direct_vm):
    direct_vm.clear_mocks()
    direct_vm.mock_web(
        "https://deliverable.example/c001.txt",
        {"status": 200, "body": TEXT_DELIVERABLE},
    )
    direct_vm.mock_web(
        "https://evidence.example/c001.txt",
        {"status": 200, "body": EVIDENCE},
    )
    direct_vm.mock_llm(
        r"You are independently assessing a milestone escrow",
        json.dumps({
            "deliverable_match": "unclear",
            "evidence_support": "yes",
            "risk": "unclear",
            "confidence": 60,
            "rationale": "The committed material is valid but the milestone criterion remains uncertain.",
        }),
    )


def mock_infrastructure_failure(direct_vm):
    direct_vm.clear_mocks()
    direct_vm.mock_web(
        "https://deliverable.example/c001.txt",
        {"status": 503, "body": b""},
    )


def mock_approval(direct_vm):
    direct_vm.clear_mocks()
    direct_vm.mock_web(
        "https://deliverable.example/c001.txt",
        {"status": 200, "body": TEXT_DELIVERABLE},
    )
    direct_vm.mock_web(
        "https://evidence.example/c001.txt",
        {"status": 200, "body": EVIDENCE},
    )
    direct_vm.mock_llm(
        r"You are independently assessing a milestone escrow",
        json.dumps({
            "deliverable_match": "yes",
            "evidence_support": "yes",
            "risk": "no",
            "confidence": 92,
            "rationale": "The committed work and evidence satisfy the brief.",
        }),
    )
    direct_vm.mock_web(
        "https://evidence.example/c001.txt",
        {"status": 200, "body": EVIDENCE},
    )


def test_submission_validation_guards_run_after_acceptance(
    direct_vm, direct_deploy, direct_alice, direct_bob
):
    contract = new_contract(direct_vm, direct_deploy)
    fund(contract, direct_vm, direct_alice, direct_bob)
    activate(contract, direct_vm, direct_bob)

    with direct_vm.expect_revert():
        contract.submit_delivery(
            "C-001", "text",
            "https://deliverable.example/c001.txt", "0x1234",
            "https://evidence.example/c001.txt", digest(EVIDENCE), "summary",
        )
    assert contract.get_milestone(public_ref(direct_alice, "C-001"))["status"] == "active"

    with direct_vm.expect_revert():
        contract.submit_delivery(
            "C-001", "text",
            "https://deliverable.example/c001.txt", digest(TEXT_DELIVERABLE),
            "https://deliverable.example/evidence.txt", digest(EVIDENCE), "summary",
        )
    assert contract.get_milestone(public_ref(direct_alice, "C-001"))["status"] == "active"

    with direct_vm.expect_revert():
        contract.submit_delivery(
            "C-001", "video",
            "https://deliverable.example/c001.mp4", digest(TEXT_DELIVERABLE),
            "https://evidence.example/c001.txt", digest(EVIDENCE), "summary",
        )
    assert contract.get_milestone(public_ref(direct_alice, "C-001"))["status"] == "active"


def test_submit_sender_guard_runs_from_active_state(
    direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie
):
    contract = new_contract(direct_vm, direct_deploy)
    fund(contract, direct_vm, direct_alice, direct_bob)
    activate(contract, direct_vm, direct_bob)

    direct_vm.sender = direct_charlie
    with direct_vm.expect_revert():
        contract.submit_delivery(
            "C-001", "text",
            "https://deliverable.example/c001.txt", digest(TEXT_DELIVERABLE),
            "https://evidence.example/c001.txt", digest(EVIDENCE), "summary",
        )
    assert contract.get_milestone(public_ref(direct_alice, "C-001"))["status"] == "active"


def test_url_guards_run_after_acceptance(
    direct_vm, direct_deploy, direct_alice, direct_bob
):
    contract = new_contract(direct_vm, direct_deploy)
    fund(contract, direct_vm, direct_alice, direct_bob)
    activate(contract, direct_vm, direct_bob)

    invalid_urls = (
        "http://example.com/file",
        "https://127.0.0.1/file",
        "https://10.1.2.3/file",
        "https://192.168.1.10/file",
        "https://169.254.10.1/file",
        "https://[::1]/file",
        "https://localhost/file",
        "https://intranet.local/file",
        "https://user@example.com/file",
        "https://example.com:8443/file",
    )
    for url in invalid_urls:
        with direct_vm.expect_revert():
            contract.submit_delivery(
                "C-001", "text", url, digest(TEXT_DELIVERABLE),
                "https://evidence.example/c001.txt", digest(EVIDENCE), "summary",
            )
        assert contract.get_milestone("C-001")["status"] == "active"


def test_mixed_failure_budgets_are_independent_and_uncertainty_exhaustion_refunds(
    direct_vm, direct_deploy, direct_alice, direct_bob
):
    contract = new_contract(direct_vm, direct_deploy)
    fund(contract, direct_vm, direct_alice, direct_bob)
    submit(contract, direct_vm, direct_bob)
    direct_vm.sender = direct_alice

    mock_uncertain(direct_vm)
    contract.review("C-001")
    saved = contract.get_milestone("C-001")
    assert saved["status"] == "retryable"
    assert int(saved["semantic_attempts"]) == 1
    assert int(saved["infrastructure_attempts"]) == 0

    direct_vm.warp("2026-10-01T12:15:00Z")
    mock_infrastructure_failure(direct_vm)
    contract.review("C-001")
    saved = contract.get_milestone("C-001")
    assert int(saved["semantic_attempts"]) == 1
    assert int(saved["infrastructure_attempts"]) == 1

    direct_vm.warp("2026-10-01T12:30:00Z")
    mock_uncertain(direct_vm)
    contract.review("C-001")
    saved = contract.get_milestone("C-001")
    assert int(saved["semantic_attempts"]) == 2
    assert int(saved["infrastructure_attempts"]) == 1

    direct_vm.warp("2026-10-01T12:45:00Z")
    mock_infrastructure_failure(direct_vm)
    contract.review("C-001")
    saved = contract.get_milestone("C-001")
    assert int(saved["semantic_attempts"]) == 2
    assert int(saved["infrastructure_attempts"]) == 2

    direct_vm.warp("2026-10-01T13:00:00Z")
    mock_uncertain(direct_vm)
    contract.review("C-001")
    saved = contract.get_milestone("C-001")
    assert saved["status"] == "blocked"
    assert saved["last_reason"] == "semantic_uncertainty_sponsor_refund"
    assert int(saved["semantic_attempts"]) == 3
    assert int(saved["infrastructure_attempts"]) == 2

    contract.settle("C-001")
    saved = contract.get_milestone("C-001")
    assert saved["status"] == "refund_dispatched"
    assert saved["settlement"] == "sponsor_refund_dispatched"
    assert int(saved["sponsor_dispatched_amount"]) == SPONSOR_AMOUNT
    assert int(saved["beneficiary_dispatched_amount"]) == 0
    assert int(saved["dispatched_amount"]) == SPONSOR_AMOUNT
    assert int(saved["deposited"]) == 0


def test_counta_has_no_inconclusive_or_split_dispatch_state(direct_vm, direct_deploy):
    contract = new_contract(direct_vm, direct_deploy)
    info = contract.get_info()
    assert "semantic_uncertainty_split_bps" not in info
    source = Path(CONTRACT).read_text(encoding="utf-8")
    for forbidden in (
        "INCONCLUSIVE =", "SPLIT_DISPATCHED =", "RESULT_INCONCLUSIVE =",
        "semantic_uncertainty_split_bps", "uncertainty_split_dispatched",
    ):
        assert forbidden not in source


def test_ten_infrastructure_failures_are_non_authorizing_bounded_telemetry_and_recoverable(
    direct_vm, direct_deploy, direct_alice, direct_bob
):
    contract = new_contract(direct_vm, direct_deploy)
    fund(contract, direct_vm, direct_alice, direct_bob)
    submit(contract, direct_vm, direct_bob)
    direct_vm.sender = direct_alice

    for index in range(10):
        hour = 12 + (index * 15) // 60
        minute = (index * 15) % 60
        timestamp = f"2026-10-01T{hour:02d}:{minute:02d}:00Z"
        direct_vm.warp(timestamp)
        mock_infrastructure_failure(direct_vm)
        contract.review("C-001")
        saved = contract.get_milestone("C-001")
        assert saved["status"] == "retryable"
        assert saved["last_reason"] == "fetch_unavailable"
        assert int(saved["semantic_attempts"]) == 0
        assert int(saved["infrastructure_attempts"]) == min(index + 1, 3)
        assert int(saved["deposited"]) == SPONSOR_AMOUNT

    saved = contract.get_milestone("C-001")
    assert saved["status"] == "retryable"
    with direct_vm.expect_revert():
        contract.settle("C-001")
    with direct_vm.expect_revert():
        contract.expire("C-001")

    # Ten outage observations did not consume semantic attempts or disable a
    # later sponsor-triggered review after the 15-minute cooldown.
    direct_vm.warp("2026-10-01T14:30:00Z")
    mock_approval(direct_vm)
    contract.review("C-001")
    saved = contract.get_milestone("C-001")
    assert saved["status"] == "approved"
    assert int(saved["semantic_attempts"]) == 0
    assert int(saved["infrastructure_attempts"]) == 3
    contract.settle("C-001")
    saved = contract.get_milestone("C-001")
    assert saved["status"] == "payout_dispatched"
    assert int(saved["deposited"]) == 0
    assert int(saved["beneficiary_dispatched_amount"]) == SPONSOR_AMOUNT
    assert int(saved["sponsor_dispatched_amount"]) == 0


def test_beneficiary_infrastructure_failures_do_not_lock_out_sponsor(
    direct_vm, direct_deploy, direct_alice, direct_bob
):
    contract = new_contract(direct_vm, direct_deploy)
    fund(contract, direct_vm, direct_alice, direct_bob)
    submit(contract, direct_vm, direct_bob)
    direct_vm.sender = direct_bob
    for timestamp in ("2026-10-01T12:00:00Z", "2026-10-01T12:15:00Z", "2026-10-01T12:30:00Z"):
        direct_vm.warp(timestamp)
        mock_infrastructure_failure(direct_vm)
        contract.review("C-001")
        saved = contract.get_milestone("C-001")
        assert saved["status"] == "retryable"
        assert int(saved["semantic_attempts"]) == 0
    direct_vm.warp("2026-10-01T12:45:00Z")
    direct_vm.sender = direct_alice
    mock_approval(direct_vm)
    contract.review("C-001")
    assert contract.get_milestone("C-001")["status"] == "approved"
    contract.settle("C-001")
    saved = contract.get_milestone("C-001")
    assert saved["status"] == "payout_dispatched"
    assert int(saved["beneficiary_dispatched_amount"]) == SPONSOR_AMOUNT
    assert int(saved["deposited"]) == 0


def test_exact_review_deadline_rejects_review_and_allows_deadline_refund(
    direct_vm, direct_deploy, direct_alice, direct_bob
):
    contract = new_contract(direct_vm, direct_deploy)
    fund(contract, direct_vm, direct_alice, direct_bob)
    submit(contract, direct_vm, direct_bob)
    direct_vm.warp("2026-10-01T18:00:00Z")
    with direct_vm.expect_revert():
        contract.review("C-001")
    contract.expire("C-001")
    saved = contract.get_milestone("C-001")
    assert saved["status"] == "refund_dispatched"
    assert saved["settlement"] == "deadline_refund_dispatched"
    assert int(saved["deposited"]) == 0
    assert int(saved["sponsor_dispatched_amount"]) == SPONSOR_AMOUNT
    assert int(saved["beneficiary_dispatched_amount"]) == 0


def test_nominated_beneficiary_alias_is_not_created_until_acceptance(
    direct_vm, direct_deploy, direct_alice, direct_bob
):
    contract = new_contract(direct_vm, direct_deploy)
    ref = fund(contract, direct_vm, direct_alice, direct_bob, "VICTIM-ALIAS")

    direct_vm.sender = direct_bob
    with direct_vm.expect_revert():
        contract.get_milestone("VICTIM-ALIAS")
    assert contract.get_milestone(ref)["status"] == "funded"

    contract.accept_milestone(ref)
    assert contract.get_milestone("VICTIM-ALIAS")["milestone_ref"] == ref
    assert contract.get_milestone(ref)["status"] == "active"


def test_accepted_beneficiary_collisions_are_ambiguous_but_canonical_refs_work(
    direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie
):
    contract = new_contract(direct_vm, direct_deploy)
    ref_a = fund(contract, direct_vm, direct_alice, direct_bob, "SHARED-ALIAS")
    direct_vm.sender = direct_charlie
    direct_vm.value = SPONSOR_AMOUNT
    ref_b = contract.create_milestone(
        "SHARED-ALIAS", direct_bob, "Second scoped item.", "evidence-b.example",
        DELIVER_BY, REVIEW_WINDOW,
    )
    direct_vm.value = 0
    direct_vm.sender = direct_bob
    with direct_vm.expect_revert():
        contract.get_milestone("SHARED-ALIAS")
    contract.accept_milestone(ref_a)
    assert contract.get_milestone("SHARED-ALIAS")["milestone_ref"] == ref_a
    assert contract.get_milestone(ref_a)["status"] == "active"
    assert contract.get_milestone(ref_b)["status"] == "funded"
    contract.accept_milestone(ref_b)
    with direct_vm.expect_revert():
        contract.get_milestone("SHARED-ALIAS")
    assert contract.get_milestone(ref_a)["milestone_ref"] == ref_a
    assert contract.get_milestone(ref_b)["milestone_ref"] == ref_b
