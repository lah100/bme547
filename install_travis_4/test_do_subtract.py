import pytest
@pytest.mark.parametrize("a, b, expected", [(3, 2, 1)])

def test_add(a, b, expected):
    from do_subtract import subtract
    answer = subtract(a, b)
    assert answer == expected
