from pathlib import Path
import ast
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_VERSION = "0.3.1"
EXPECTED_CONTRACT_SHA256 = "9b98e0016a38e7c4ad8e613370b0667e7c4b37910e4dbaf26e99a6a1688be005"
CONTRACTS = ROOT / "contracts"
SOURCES = sorted(CONTRACTS.glob("*.py"))
if len(SOURCES) != 1 or SOURCES[0].name != "counta.py":
    raise SystemExit(f"release gate requires exactly contracts/counta.py; found {[p.name for p in SOURCES]}")

source = SOURCES[0]
raw = source.read_bytes()
ast.parse(raw.decode("utf-8"), filename=str(source))
header = raw.decode("utf-8").splitlines()[0].strip()
version_match = re.fullmatch(r"# v(\d+\.\d+\.\d+)", header)
if not version_match:
    raise SystemExit("contract version header is missing or malformed")
if version_match.group(1) != EXPECTED_VERSION:
    raise SystemExit(f"release gate expects Counta {EXPECTED_VERSION}")
contract_sha256 = hashlib.sha256(raw).hexdigest()
if contract_sha256 != EXPECTED_CONTRACT_SHA256:
    raise SystemExit(
        "frozen contract source hash mismatch: "
        f"expected {EXPECTED_CONTRACT_SHA256}, got {contract_sha256}"
    )
subprocess.run([sys.executable, "-m", "compileall", "-q", "contracts", "tests"], cwd=ROOT, check=True)

lint = shutil.which("genvm-lint") or shutil.which("genvm-lint.exe")
if not lint:
    candidate = Path(sys.executable).with_name("genvm-lint.exe" if sys.platform == "win32" else "genvm-lint")
    if candidate.exists():
        lint = str(candidate)
if not lint:
    raise SystemExit("genvm-lint is required for preflight; install requirements.txt")

subprocess.run([lint, "check", str(source), "--json"], cwd=ROOT, check=True)
committed_abi = ROOT / "artifacts" / "counta.abi.json"
if not committed_abi.is_file():
    raise SystemExit("tracked ABI artifact is missing: artifacts/counta.abi.json")
with tempfile.TemporaryDirectory(prefix="counta-schema-") as schema_dir:
    generated_abi = Path(schema_dir) / "counta.abi.json"
    subprocess.run([lint, "schema", str(source), "--output", str(generated_abi)], cwd=ROOT, check=True)
    if generated_abi.read_bytes() != committed_abi.read_bytes():
        raise SystemExit("generated ABI differs from committed artifacts/counta.abi.json")
print("abi_matches_committed_artifact=PASS")
test = subprocess.run(
    [sys.executable, "-m", "pytest", "tests/direct", "-q"],
    cwd=ROOT, capture_output=True, text=True,
)
print(test.stdout, end="")
print(test.stderr, end="", file=sys.stderr)
if test.returncode:
    raise SystemExit(test.returncode)
summary = test.stdout + "\n" + test.stderr
match = re.search(r"(?:^|\s)(\d+) passed(?:,\s*(\d+) skipped)?(?:,\s*(\d+) failed)?\s+in\s", summary)
if not match:
    raise SystemExit("could not verify pytest test-count summary")
passed, skipped, failed = (int(value or 0) for value in match.groups())
if skipped or failed:
    raise SystemExit(f"release tests must not skip or fail: passed={passed}, skipped={skipped}, failed={failed}")
print("contract_version=" + version_match.group(1))
print("contract_sha256=" + contract_sha256)
print("contract_source_bytes=" + str(len(raw)))
print("direct_mode_tests=" + str(passed))
print("tests_skipped=" + str(skipped))
print("tests_failed=" + str(failed))
print("deployable_contract_sources=1")
print("abi_matches=PASS")
print("preflight=PASS")
