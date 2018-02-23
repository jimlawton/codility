
def solution(A):
    values = sorted(set(A))
    for value in values:
        if A.count(value) == 1:
            return value
    return 0

