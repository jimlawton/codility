
from challenge import solution


def test_challenge():
    assert solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) == 6
    assert solution(5, [1, 3, 5, 4, 2, 3, 1, 4]) == 4
    assert solution(5, [5, 4, 3, 2, 1, 3, 1, 4]) == 4
    assert solution(2, [1, 3, 2]) == 2
    assert solution(2, [1]) == -1
    assert solution(2, [1, 1]) == -1
    assert solution(5, [1, 3, 1, 4, 2, 3, 1, 4]) == -1
