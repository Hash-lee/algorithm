import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# 1 <= N <= 50
# L <= diff <=R
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def BFS(r, c):
    global flag
    Q = deque([(r, c)])
    union = [(r, c)]
    total = arr[r][c]
    while Q:
        cr, cc = Q.pop()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0 <= nr < N and 0 <= nc < N and L <= abs(arr[cr][cc] - arr[nr][nc]) <= R and visited[nr][nc]:
                visited[nr][nc] = 0
                union.append((nr, nc))
                Q.append((nr, nc))
                total += arr[nr][nc]
                flag = True

    if flag:
        k = total // len(union)
        while union:
            r, c = union.pop()
            arr[r][c] = k


flag = True
day = 0
while flag:
    flag = False
    visited = [[1] * N for _ in range(N)]
    for r in range(0, N):
        for c in range(0, N):
            if visited[r][c]:
                visited[r][c] = 0
                BFS(r, c)
    if flag:
        day += 1

print(day)