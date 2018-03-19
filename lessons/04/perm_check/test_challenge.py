
from challenge import solution


def test_challenge():
    assert solution([4]) == 0
    assert solution([1]) == 1
    assert solution([4, 1, 3, 2]) == 1
    assert solution([4, 1, 3]) == 0
