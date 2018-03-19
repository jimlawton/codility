
from challenge import solution

# Example tests, will be different for different input types

def test_challenge_array():
    assert(solution([3, 1]) == 2)
    assert(solution([3, 1, 2, 4, 3]) == 1)
    assert(solution([-10, -20, -30, -40, 100]) == 20)
