
def solution(A, K):
    if K == 0 or K == len(A): 
        return A
    if K > 1:
        a = A[K-1:] + A[:K-1]
    else:
        a = A[1:] + [A[0]]
    return a
