import sys
from collections import deque

N = int(sys.stdin.readline())
Sr, Sc, Fr, Fc = list(map(int, sys.stdin.readline().split()))
dir_r = [-2, -2, 0, 0, 2, 2]
dir_c = [-1, 1, -2, 2, -1, 1]
visit = [[1] * N for _ in range(N)]
Q = deque()
Q.append((Sr, Sc, 1))
visit[Sr][Sc] = 0
while Q:
    r, c, t = Q.popleft()
    for k in range(6):
        nr = r + dir_r[k]
        nc = c + dir_c[k]
        if 0 <= nr < N and 0 <= nc < N and visit[nr][nc]:
            if (nr, nc) == (Fr, Fc):
                print(t)
                exit()
            else:
                visit[nr][nc] = 0
                Q.append((nr, nc, t + 1))

print(-1)