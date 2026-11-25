import subprocess
import sys
from pathlib import Path

def run_cli(*args):
    return subprocess.run(
        [sys.executable, "calculator.py", *args],
        cwd=Path(__file__).parent, capture_output=True, text=True, check=False
    )

def test_cli_expression_mode():
    result = run_cli("--expression", "sqrt(25) + 2")
    assert result.returncode == 0
    assert result.stdout.strip() == "7"

def test_cli_radian_mode():
    result = run_cli("--expression", "sin(pi / 2)", "--angle-mode", "RAD")
    assert result.returncode == 0
    assert float(result.stdout.strip()) == 1.0

def test_cli_division_by_zero_returns_error_code():
    result = run_cli("--expression", "1 / 0")
    assert result.returncode == 1
    assert "Cannot divide by zero" in result.stdout
