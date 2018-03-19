
from challenge import solution


def test_challenge_array():
    assert(solution([1, 3, 6, 4, 1, 2])) == 5
    assert(solution([1, 2, 3])) == 4
    assert(solution([-1, -3])) == 1
