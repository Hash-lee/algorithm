import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
start = tuple(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
end = tuple(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
visit = [[[-1] * 4 for _ in range(C)] for _ in range(R)]
r, c, d = start
visit[r][c][d] = 0

Q = deque([start])
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
while True:
    r, c, d = Q.popleft()
    if (r, c, d) == end:
        print(visit[r][c][d])
        exit()
    for k in range(4):
        if k == d:
            for i in range(1, 4):
                nr = r + dr[k] * i
                nc = c + dc[k] * i
                if not (0 <= nr < R and 0 <= nc < C) or arr[nr][nc]: break
                if visit[nr][nc][d] == -1 or visit[r][c][d] + 1 < visit[nr][nc][d]:
                    visit[nr][nc][d] = visit[r][c][d] + 1
                    Q.append((nr, nc, d))
        else:
            if d == 0 and k == 1: continue
            if d == 1 and k == 0: continue
            if d == 2 and k == 3: continue
            if d == 3 and k == 2: continue
            if visit[r][c][k] == -1 or visit[r][c][d] + 1 < visit[r][c][k]:
                visit[r][c][k] = visit[r][c][d] + 1
                Q.append((r, c, k))