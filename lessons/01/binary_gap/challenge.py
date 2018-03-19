
def solution(N):
    maxgap = 0
    # Ignore the '0b' at the beginning.
    inlst = list(bin(N))[2:]
    # Convert to ints.
    inlst = [int(x) for x in inlst]
    if inlst.count(0) == 0:
        # print(n, 0)
        return 0
    gap = 0
    ingap = False
    start = 0
    for i,bitval in enumerate(inlst):
        if bitval == 1:
            if not ingap:
                continue
            ingap = False
            gap = i - start
        else:
            if ingap:
                continue
            ingap = True
            start = i
        maxgap = max(gap, maxgap)
    # print(n, maxgap)
    return maxgap

