from app import calculate_results

def test_calculation():
    results = calculate_results([80, 90, 70])
    assert results["total"] == 240
    assert results["average"] == 80.0
