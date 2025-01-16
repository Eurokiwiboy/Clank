from src.automation.simulate_command import simulate

def test_simulate_short():
    result = simulate("Describe the benefits of exercise.", "short")
    assert result == "Exercise helps improve physical and mental health."

def test_simulate_detailed():
    result = simulate("Describe the benefits of exercise.", "detailed")
    assert result.startswith("Exercise offers a range of benefits")
