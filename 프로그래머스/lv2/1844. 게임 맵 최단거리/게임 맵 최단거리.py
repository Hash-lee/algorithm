from collections import deque

def solution(maps):
    R, C = len(maps), len(maps[0])
    Q = deque([(0, 0, 1)])
    maps[0][0] = 0
    
    des = (R-1, C-1)
    move = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while Q:
        r, c, move = Q.popleft()
        if (r, c) == des: return move
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C and maps[nr][nc]:
                Q.append((nr, nc, move+1))
                maps[nr][nc] = 0
    return -1