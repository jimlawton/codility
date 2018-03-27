# A non-empty zero-indexed array A consisting of N integers is given. A pair
# of integers (P, Q), such that 0 <= P < Q < N, is called a slice of array A
# (notice that the slice contains at least two elements). The average of a
# slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the
# length of the slice. To be precise, the average equals
# (A[P] + A[P + 1] + ... + A[Q]) / (Q - P + 1).
#
# For example, array A such that:
#     A = [4, 2, 2, 5, 1, 5, 8]
# contains the following example slices:
#  * slice (1, 2), whose average is (2 + 2) / 2 = 2;
#  * slice (3, 4), whose average is (5 + 1) / 2 = 3;
#  * slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
# The goal is to find the starting position of a slice whose average is
# minimal.
#
# Write a function:
#   def solution(A)
# that, given a non-empty zero-indexed array A consisting of N integers,
# returns the starting position of the slice with the minimal average. If
# there is more than one slice with a minimal average, you should return the
# smallest starting position of such a slice.
#
# For example, given array A such that:
#     A = [4, 2, 2, 5, 1, 5, 8]
# the function should return 1, as explained above.
#
# Assume that:
#  * N is an integer within the range [2..100,000];
#  * each element of array A is an integer within the range [-10,000..10,000].
#
# Complexity:
#  * expected worst-case time complexity is O(N);
#  * expected worst-case space complexity is O(N), beyond input storage
#    (not counting the storage required for input arguments).


def prefix_sums(A):
    n = len(A)
    p = [0] * (n + 1)
    for k in range(1, n+1):
        p[k] = p[k-1] + A[k-1]
    return p


def suffix_sums(A):
    n = len(A)
    s = [0] * (n + 1)
    for k in range(n, 0, -1):
        s[k-1] = s[k] + A[k-1]
    return s


def count_total(p, x, y):
    return p[y+1] - p[x]


def solution(A):
    p = prefix_sums(A)
    print("prefix sums: %s" % p)
    s = suffix_sums(A)
    print("suffix sums: %s" % s)
    return 0
