import sys
from heapq import heapify, heappop, heappush

N, K = map(int, sys.stdin.readline().split())
treasure = []
bags = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    treasure.append((M, V))
treasure.sort()
heapify(treasure)

for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()
heapify(bags)

ans = 0
available = []
for _ in range(K):
    limit = heappop(bags)
    while treasure and treasure[0][0] <= limit:
        w, v = heappop(treasure)
        heappush(available, -v)
    if available:
        ans -= heappop(available)

print(ans)