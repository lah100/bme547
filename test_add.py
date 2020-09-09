import pytest
@pytest.mark.parametrize("a, b, expected", [(1,2,3), (2,2,5)])
def test_do_add(a, b, expected):
	from add import do_add
	answer = do_add(a, b)
	assert answer == expected
