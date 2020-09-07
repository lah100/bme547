import pytest
@pytest.mark.parametrize("x1, y1, x2, y2, new_x, expected", [(0,0,1,1,2,2), (0,0,1,1,2,5), (0,1,3,3,6,5)])

def test_output_y(x1, y1, x2, y2, new_x, expected):
    from coordinateout import output_y
    answer = output_y(x1, y1, x2, y2, new_x)
    assert answer == expected



