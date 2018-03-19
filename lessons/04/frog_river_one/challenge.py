# A small frog wants to get to the other side of a river. The frog is
# initially located on one bank of the river (position 0) and wants to get to
# the opposite bank (position X+1). Leaves fall from a tree onto the surface of
# the river.
#
# You are given a zero-indexed array A consisting of N integers representing
# the falling leaves. A[K] represents the position where one leaf falls at time
# K, measured in seconds.
#
# The goal is to find the earliest time when the frog can jump to the other
# side of the river. The frog can cross only when leaves appear at every
# position across the river from 1 to X (that is, we want to find the earliest
# moment when all the positions from 1 to X are covered by leaves). You may
# assume that the speed of the current in the river is negligibly small, i.e.
# the leaves do not change their positions once they fall in the river.
#
# For example, you are given integer X = 5 and array A such that:
#   A = [1, 3, 1, 4, 2, 3, 5, 4]
# In second 6, a leaf falls into position 5. This is the earliest time when
# leaves appear in every position across the river.
#
# Write a function:
#   def solution(X, A)
# that, given a non-empty zero-indexed array A consisting of N integers and
# integer X, returns the earliest time when the frog can jump to the other
# side of the river.
#
# If the frog is never able to jump to the other side of the river, the
# function should return −1.
#
# For example, given X = 5 and array A such that:
#   A = [1, 3, 1, 4, 2, 3, 5, 4]
# the function should return 6, as explained above.
#
# Assume that:
# * N and X are integers within the range [1..100,000];
# * each element of array A is an integer within the range [1..X].
#
# Complexity:
#  * expected worst-case time complexity is O(N);
#  * expected worst-case space complexity is O(X), beyond input storage (not
#    counting the storage required for input arguments).


def solution(X, A):
    N = len(A)
    if N < X:
        return -1
    leaves = [0] * X
    covered = 0
    # print("leaves: %s" % (leaves))
    for i in range(0, N):
        if A[i] > X:
            continue
        if leaves[A[i]-1] == 0:
            leaves[A[i]-1] = 1
            covered += 1
        # print("leaves: %s" % (leaves))
        if covered == X:
            return i
    return -1