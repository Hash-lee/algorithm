import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
p = []
q = []
np = 0
nq = 0
for _ in range(N):
    heappush(q, int(sys.stdin.readline()))
    nq += 1
    if 2 < nq - np:
        heappush(p, -heappop(q))
        nq -= 1
        np += 1
    while p and q and q[0] < -p[0]:
        heappush(q, -heappop(p))
        heappush(p, -heappop(q))
    print(q[0])