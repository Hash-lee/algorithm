import sys
from collections import deque

T = int(sys.stdin.readline())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, T+1):
    ans = 0
    R, C = map(int, sys.stdin.readline().split())
    visit = [[True]*C for _ in range(R)]
    arr = [sys.stdin.readline().strip() for _ in range(R)]
    keys = sys.stdin.readline().strip()
    keys = set() if keys == "0" else set(keys)
    accessible_locks = {}

    Q = deque()
    for c in range(C):
        if arr[0][c] != "*":
            Q.append((0, c))
            visit[0][c] = False
        if arr[R-1][c] != "*":
            Q.append((R-1, c))
            visit[R-1][c] = False
    for r in range(1, R-1):
        if arr[r][0] != "*":
            Q.append((r, 0))
            visit[r][0] = False
        if arr[r][C-1] != "*":
            Q.append((r, C-1))
            visit[r][C-1] = False
    
    while Q:
        r, c = Q.popleft()
        code = ord(arr[r][c])
        if code == 36:
            ans += 1
        if 65 <= code <= 90 and not chr(code+32) in keys:
            if chr(code) in accessible_locks:
                accessible_locks[chr(code)].append((r, c))
            else:
                accessible_locks[chr(code)] = [(r, c)]
            continue
        if 97 <= code <= 122:
            keys.add(chr(code))
            if chr(code-32) in accessible_locks:
                Q.extend(accessible_locks[chr(code-32)])
                del accessible_locks[chr(code-32)]
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C and visit[nr][nc]:
                if arr[nr][nc] != "*":
                    Q.append((nr, nc))
                    visit[nr][nc] = False
    print(ans)