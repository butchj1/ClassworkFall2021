import pytest


@pytest.mark.parametrize("HDL_value, expected", [
    (65, "Normal"),
    (45, "Borderline Low"),
    (30, "Low")])


def test_HDL_analysis(HDL_value, expected):
    from blood_calculator import HDL_analysis
    answer = HDL_analysis(HDL_value)
    assert answer == expected
