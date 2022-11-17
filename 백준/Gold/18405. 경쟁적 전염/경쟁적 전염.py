import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
virus_Q = deque()

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

tmp = []
for r in range(N):
    for c in range(N):
        if arr[r][c]:
            tmp.append((arr[r][c], r, c))

tmp.sort()
virus_Q.extend(tmp)

S, X, Y = map(int, sys.stdin.readline().split())

dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]
for _ in range(S):
    for _ in range(len(virus_Q)):
        virus, row, col = virus_Q.popleft()
        for k in range(4):
            nr = row + dir_r[k]
            nc = col + dir_c[k]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
                arr[nr][nc] = virus
                virus_Q.append((virus, nr, nc))

print(arr[X - 1][Y - 1])
