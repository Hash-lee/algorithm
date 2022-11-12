import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())


connection = 0
arr = [[0 for _ in range(N + 1)] for __ in range(N + 1)]
visit = [1] * (N + 1)
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    arr[s][e], arr[e][s] = 1, 1


def DFS(r):
    for c in range(N + 1):
        if arr[r][c] and visit[c]:
            visit[c] = 0
            DFS(c)


for i in range(1, N + 1):
    if visit[i]:
        visit[i] = 0
        connection += 1
        DFS(i)

print(connection)
