import pytest


@pytest.mark.parametrize("x1, y1, x2, y2, x, expected", [
    (0, 0, 10, 10, 5, 5),
    (0, 0, 10, 20, 5, 10),
    (0, 0, 10, 30, 5, 15)])
def test_y_return(x1, y1, x2, y2, x, expected):
    from coordinates import y_return
    answer = y_return(x1, y1, x2, y2, x)
    assert answer == expected
