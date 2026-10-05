from pathlib import Path
import ast
import hashlib
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "contracts"
SOURCES = sorted(CONTRACTS.glob("*.py"))
if len(SOURCES) != 1 or SOURCES[0].name != "counta.py":
    raise SystemExit(f"release gate requires exactly contracts/counta.py; found {[p.name for p in SOURCES]}")

source = SOURCES[0]
raw = source.read_bytes()
ast.parse(raw.decode("utf-8"), filename=str(source))
subprocess.run([sys.executable, "-m", "compileall", "-q", "contracts", "tests"], cwd=ROOT, check=True)
subprocess.run([sys.executable, "-m", "pytest", "tests/direct", "-q"], cwd=ROOT, check=True)

lint = shutil.which("genvm-lint") or shutil.which("genvm-lint.exe")
if not lint:
    candidate = Path(sys.executable).with_name("genvm-lint.exe" if sys.platform == "win32" else "genvm-lint")
    if candidate.exists():
        lint = str(candidate)
if not lint:
    raise SystemExit("genvm-lint is required for preflight; install requirements.txt")

subprocess.run([lint, "check", str(source), "--json"], cwd=ROOT, check=True)
(ROOT / "artifacts").mkdir(exist_ok=True)
subprocess.run([lint, "schema", str(source), "--output", "artifacts/counta.abi.json"], cwd=ROOT, check=True)
print("contract_sha256=" + hashlib.sha256(raw).hexdigest())
print("deployable_contract_sources=1")
print("preflight=PASS")
