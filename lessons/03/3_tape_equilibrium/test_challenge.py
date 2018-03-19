
from challenge import solution

# Example tests, will be different for different input types

def test_challenge_array():
    # Test empty array (dependent on test)
    # Test single entry array
    assert solution([]) == []


# Benchmark

def test_challenge_a(benchmark):
    assert benchmark(solution, 1) == 1


def test_challenge_b(benchmark):
    assert benchmark(solution, 2147483647) == 2147483647
