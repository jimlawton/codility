
def solution(A, K):
    if K == 0 or K == len(A): 
        return A
    a = A[K-1:] + A[:K-1]
    return a
