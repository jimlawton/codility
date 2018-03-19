# This is a demo task.

# Write a function:
#   def solution(A)
# that, given an array A of N integers, returns the smallest positive integer
# (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [-1, -3], the function should return 1.

# Assume that:
#  * N is an integer within the range [1..100,000];
#  * each element of array A is an integer within the range
#    [-1,000,000..1,000,000].

# Complexity:
#  * expected worst-case time complexity is O(N);
#  * expected worst-case space complexity is O(N), beyond input storage
#    (not counting the storage required for input arguments).


def solution(A):
    N = len(A)
    if N == 1:
        if A[0] > 1:
            return 1
    poscount = [0] * 1000001
    negcount = [0] * 1000001
    for k in range(N):
        # print(A[k])
        if A[k] >= 0:
            poscount[A[k]] += 1
        else:
            negcount[-A[k]] += 1
        # print(poscount, negcount)
    if sum(poscount) == 0:
        return 1
    for i in range(1, len(poscount)):
        if poscount[i] == 0:
            return i
    return len(poscount)
