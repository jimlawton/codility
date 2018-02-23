
def solution(A, K):
    if K == 0 or K == len(A): 
        return A
    if K == 1:
        return A[1:] + [A[0]]
    return A[K-1:] + A[:K-1]
