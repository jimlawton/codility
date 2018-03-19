
def solution(A, K):
    if len(A) == 0 or K == 0 or K == len(A):
        return A
    K = K % len(A)
    # for i in range(K):
    #     A = [A[-1]] + A[:-1]
    #     print("%d: %s" % (i, A))
    A = A[-K:] + A[:-K]
    return A
