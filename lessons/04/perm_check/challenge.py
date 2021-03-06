# A non-empty zero-indexed array A consisting of N integers is given.
#
# A permutation is a sequence containing each element from 1 to N once, and
# only once.
#
# For example, array A such that:
#     A = [4, 1, 3, 2]
# is a permutation, but array A such that:
#     A = [4, 1, 3]
# is not a permutation, because value 2 is missing.
#
# The goal is to check whether array A is a permutation.
#
# Write a function:
#   def solution(A)
# that, given a zero-indexed array A, returns 1 if array A is a permutation
# and 0 if it is not.
#
# For example, given array A such that:
#     A = [4, 1, 3, 2]
# the function should return 1.
#
# Given array A such that:
#     A = [4, 1, 3]
# the function should return 0.
#
# Assume that:
#  * N is an integer within the range [1..100,000];
#  * each element of array A is an integer within the range [1..1,000,000,000].
#
# Complexity:
#  * expected worst-case time complexity is O(N);
#  * expected worst-case space complexity is O(N), beyond input storage (not
#    counting the storage required for input arguments).


def solution(A):
    N = len(A)
    if N == 1:
        if A[0] == 1:
            return 1
        else:
            return 0
    count = {}
    for i in range(N):
        if A[i] not in count:
            count[A[i]] = 0
        count[A[i]] += 1
        if count[A[i]] > 1:
            return 0
    # print(count)
    values = count.keys()
    # print(values)
    if max(values) == N:
        return 1
    return 0
