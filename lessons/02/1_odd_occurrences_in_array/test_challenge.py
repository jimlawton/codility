
from challenge import solution


def test_challenge_all():
    # Single entry slot
    assert solution([99]) == 99
    # Answer in last slot
    assert solution([2, 2, 3, 3, 4]) == 4
    # Answer in first slot
    assert solution([2, 3, 3, 4, 4]) == 2
    # Answer in middle slot
    assert solution([2, 2, 3, 4, 4]) == 3
    # Different positions
    assert solution([9, 3, 9, 3, 9, 7, 9]) == 7
    assert solution([9, 3, 9, 3, 9, 1, 9]) == 1
    assert solution([9, 1, 9, 1, 9, 2, 9]) == 2
    assert solution([9, 1, 9, 1, 9, 2, 9]) == 2


# Benchmark

def test_challenge_a(benchmark):
    assert benchmark(solution, [99]) == 99


def test_challenge_b(benchmark):
    assert benchmark(solution, [2, 2, 3, 3, 4]) == 4


def test_challenge_c(benchmark):
    assert benchmark(solution, [9, 3, 9, 3, 9, 7, 9]) == 7

