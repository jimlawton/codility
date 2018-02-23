from challenge import solution

# All

def test_challenge_all():
    assert solution(1) == 0
    assert solution(9) == 2
    assert solution(15) == 0
    assert solution(20) == 1
    assert solution(529) == 4
    assert solution(1041) == 5
    assert solution(2147483647) == 0


# Benchmark

def test_challenge_a(benchmark):
    assert benchmark(solution, 1) == 0


def test_challenge_b(benchmark):
    assert benchmark(solution, 2147483647) == 0


def test_challenge_c(benchmark):
    assert benchmark(solution, 9) == 2


def test_challenge_d(benchmark):
    assert benchmark(solution, 15) == 0


def test_challenge_e(benchmark):
    assert benchmark(solution, 20) == 1


def test_challenge_f(benchmark):
    assert benchmark(solution, 33) == 4


def test_challenge_g(benchmark):
    assert benchmark(solution, 529) == 4


def test_challenge_h(benchmark):
    assert benchmark(solution, 1041) == 5
