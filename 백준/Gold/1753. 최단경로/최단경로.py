import sys
from heapq import heappush, heappop

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
edges = {i:{} for i in range(1, V+1)}
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if v in edges[u]: edges[u][v] = min(edges[u][v], w)
    else: edges[u][v] = w

visit = [float("INF")] * (V+1)
visit[K] = 0
S = {K}
N = []
for key, value in edges[K].items():
    if visit[K] + value < visit[key]:
        visit[key] = visit[K] + value
        heappush(N, (visit[key], key))

for _ in range(V-1):
    if not N: break
    v, node = heappop(N)
    while N and node in S:
        v, node = heappop(N)
    S.add(node)

    for key, value in edges[node].items():
        if not key in S and visit[node] + value < visit[key]:
            visit[key] = visit[node] + value
            heappush(N, (visit[key], key))

for i in range(1, V+1):
    print("INF" if visit[i] == float("INF") else visit[i])