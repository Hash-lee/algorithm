import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
lake = [list(sys.stdin.readline().strip()) for _ in range(R)]

visit = [[0] * C for _ in range(R)]
swan = []
target = []
for r in range(R):
    for c in range(C):
        if lake[r][c] == "L":
            visit[r][c] = 0
            if not swan:
                swan.append((r, c))
            else:
                target.append((r, c))
            lake[r][c] = 0
        elif lake[r][c] == ".":
            lake[r][c] = 0
        elif lake[r][c] == "X":
            lake[r][c] = 1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def check(swan, n):
    temp = set()
    Q = deque(swan)
    while Q:
        r, c = Q.popleft()
        if n == -1 and (r, c) == target[0]:
            print(0)
            exit()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if visit[nr][nc] == 0:
                    if lake[nr][nc] == 0:
                        visit[nr][nc] = n
                        Q.append((nr, nc))
                    if lake[nr][nc] == 1:
                        temp.add((r, c))
    return list(temp)

def ices():
    melted = set()
    for r in range(R):
        for c in range(C):
            if lake[r][c] == 1:
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < R and 0 <= nc < C:
                        if lake[nr][nc] == 0:
                            visit[r][c] = 1
                            melted.add((r, c))
    return list(melted)


swan1 = deque(check(swan, -1))
swan2 = deque(check(target, -2))
melted = deque(ices())
day = 0
while True:
    day += 1
    next_melted = set()
    while melted:
        r, c = melted.popleft()
        lake[r][c] = 0
        visit[r][c] = 0
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if lake[nr][nc] and visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    next_melted.add((nr, nc))
    
    next_swan1 = set()
    while swan1:
        r, c = swan1.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if lake[nr][nc]:
                    next_swan1.add((nr, nc))
                else:
                    if lake[nr][nc] == 0:
                        if visit[nr][nc] == 0:
                            visit[nr][nc] = -1
                            swan1.append((nr, nc))
                        if visit[nr][nc] == -2:
                            print(day)
                            exit()

    next_swan2 = set()
    while swan2:
        r, c = swan2.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if lake[nr][nc]:
                    next_swan2.add((nr, nc))
                else:
                    if lake[nr][nc] == 0:
                        if visit[nr][nc] == 0:
                            visit[nr][nc] = -2
                            swan2.append((nr, nc))
                        if visit[nr][nc] == -1:
                            print(day)
                            exit()

    swan1 = deque(list(next_swan1))
    swan2 = deque(list(next_swan2))
    melted = deque(list(next_melted))