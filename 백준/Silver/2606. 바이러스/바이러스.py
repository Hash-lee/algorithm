import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
arr = [[0 for _ in range(N + 1)] for __ in range(N + 1)]

for _ in range(K):
    s, e = map(int, sys.stdin.readline().split())
    arr[s][e], arr[e][s] = 1, 1

visit = [1] * (N + 1)
visit[1] = 0
counts = 0


def DFS(start=1):
    for end in range(1, N+1):
        if visit[end] and arr[start][end]:
            global counts
            counts += 1
            visit[end] = 0
            DFS(end)


DFS()

print(counts)