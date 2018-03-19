
from challenge import solution

def test_challenge_array():
    assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
    assert solution([0, 0, 0], 1) == [0, 0, 0]
    assert solution([1, 2, 3, 4], 4) == [1, 2, 3, 4]
    assert solution([1, 2, 3, 4], 0) == [1, 2, 3, 4]
    assert solution([5, -1000], 1) == [-1000, 5]
    assert solution([], 1) == []
    assert solution([1, 2, 3, 4, 5, 6, 7], 2) == [6, 7, 1, 2, 3, 4, 5]


# Benchmark

def test_challenge_a(benchmark):
    assert benchmark(solution, [3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]


def test_challenge_b(benchmark):
    assert benchmark(solution, [0, 0, 0], 1) == [0, 0, 0]


def test_challenge_c(benchmark):
    assert benchmark(solution, [1, 2, 3, 4], 4) == [1, 2, 3, 4]
