from calculator_engine import SCALAR_FUNCTIONS, evaluate

def test_scalar_function_registry_contains_expected_functions():
    assert set(SCALAR_FUNCTIONS) == {"sqrt", "log", "ln"}
    assert evaluate("sqrt(49)") == 7
