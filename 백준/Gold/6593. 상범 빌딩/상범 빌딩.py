import sys
from collections import deque

dr = [0, 1, 0, -1, 0, 0]
dc = [1, 0, -1, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
dct = {"#": 9, ".": 0, "S": 1, "E": 2}


def BFS(Q):
    h, r, c, t = Q[0]
    building[h][r][c] = 9
    while Q:
        h, r, c, t = Q.popleft()
        for k in range(6):
            nh, nr, nc, nt = h + dh[k], r + dr[k], c + dc[k], t + 1
            if 0 <= nh < H and 0 <= nr < R and 0 <= nc < C:
                if not building[nh][nr][nc]:
                    building[nh][nr][nc] = 9
                    Q.append((nh, nr, nc, nt))
                elif building[nh][nr][nc] == 2:
                    return t
    return 0


def start(H, R, C):
    for h in range(H):
        for r in range(R):
            for c in range(C):
                if building[h][r][c] == 1:
                    return (h, r, c, 1)


while True:
    H, R, C = map(int, sys.stdin.readline().split())
    if H == R == C == 0:
        break
    building = []
    for _ in range(H):
        building.append([list(map(lambda x: dct[x], list(sys.stdin.readline().rstrip()))) for _ in range(R)])
        sys.stdin.readline()

    Q = deque([start(H, R, C)])
    t = BFS(Q)
    print(f"Escaped in {t} minute(s).") if t else print("Trapped!")
