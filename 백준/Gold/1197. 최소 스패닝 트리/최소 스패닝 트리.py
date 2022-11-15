import sys
from heapq import heappush, heappop

V, E = map(int, sys.stdin.readline().split())

min_distance = [10000001] * (V)
linked = [False for i in range(V)]
distance = {i: [] for i in range(V)}

for _ in range(E):
    p1, p2, d = map(int, sys.stdin.readline().split())
    distance[p1 - 1].append((d, p2 - 1))
    distance[p2 - 1].append((d, p1 - 1))


heap = []
min_distance[0] = 0
heappush(heap, (0, 0))
mn = 0
k = 0
while heap:
    mn_d, s_node = heappop(heap)
    if linked[s_node] == False:
        linked[s_node] = True
        mn += mn_d
        k += 1
        for info in distance[s_node]:
            d, e_node = info
            if d < min_distance[e_node]:
                min_distance[e_node] = d
                heappush(heap, (d, e_node))

print(mn)