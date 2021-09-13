import pytest

@pytest.mark.parametrize("x, expected", [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10)])

def test_y_return(x, expected):
    from coordinates import y_return
    answer = y_return(x)
    assert answer == expected