
from challenge import solution


def test_challenge():
    # Create empty array (dependent on test)
    # Create single entry array
    assert solution(6, 11, 2) == 3
    assert solution(0, 0, 11) == 1
    assert solution(1, 1, 11) == 0
    assert solution(10, 10, 5) == 1
    assert solution(10, 10, 7) == 0
    assert solution(10, 10, 20) == 0
