import pytest
from calculator_engine import evaluate

def test_boolean_constant_is_rejected():
    with pytest.raises(ValueError):
        evaluate("True")
