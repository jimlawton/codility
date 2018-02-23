
from challenge import solution, solutionArray

# Example tests, will be different for different input types

# FIXME Tailor to the solution input

def test_challenge_int():
    # Use 0 or 1
    # Use upper and lower limits
    assert solution(2) == 2
    assert solution(4) == 4
    assert solution(0) == 0
    assert solution(1) == 1
    assert solution(5) == 5


def test_challenge_array():
    # Create empty array (dependent on test)
    # Create single entry array
    # Create an array with the answer at the start
    # Create an array with the answer at the end
    # Create an array with the answer in the middle
    assert solutionArray([9, 3, 9, 3, 9, 7, 9]) == [9, 3, 9, 3, 9, 7, 9]
    assert solutionArray([9, 3, 9, 3, 9, 1, 9]) == [9, 3, 9, 3, 9, 1, 9]
    assert solutionArray([9, 1, 9, 1, 9, 2, 9]) == [9, 1, 9, 1, 9, 2, 9]
    assert solutionArray([9, 1, 9, 1, 9, 2, 9]) == [9, 1, 9, 1, 9, 2, 9]
    # Single entry slot
    assert solutionArray([99]) == [99]
    # Answer in last slot
    assert solutionArray([2, 2, 3, 3, 4]) == [2, 2, 3, 3, 4]
    # Answer in first slot
    assert solutionArray([2, 3, 3, 4, 4]) == [2, 3, 3, 4, 4]
    # Answer in middle slot
    assert solutionArray([2, 2, 3, 4, 4]) == [2, 2, 3, 4, 4]


# Benchmark

def test_challenge_a(benchmark):
    assert benchmark(solution, 1) == 1


def test_challenge_b(benchmark):
    assert benchmark(solution, 2147483647) == 2147483647
