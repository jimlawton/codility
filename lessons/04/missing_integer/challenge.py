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
    count = [0] * (N + 1)
    if N == 1:
        if A[0] > 1:
            return 1
    for k in range(N):
        count[A[k]] += 1
        # print(count)
    for i in range(1, len(count)):
        if count[i] == 0:
            return i
    return len(count)
