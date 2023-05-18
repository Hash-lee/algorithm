import sys
R, C = map(int, sys.stdin.readline().split())
arr = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(R)]
visited = [[True] * C for _ in range(R)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def fill(y, x):
    Q =[(y, x)]
    adj = set()
    front = -1
    rear = 0
    while front < rear:
        front += 1
        r, c = Q[front]
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if arr[nr][nc] == 0 and visited[nr][nc]:
                    visited[nr][nc] = False
                    Q.append((nr, nc))
                    rear += 1
                elif arr[nr][nc]:
                    adj.add(nr * 10000 + nc)
    rear += 1
    for code in sorted(adj):
        r, c = code // 10000, code % 10000
        arr[r][c] += rear


for r in range(R):
    for c in range(C):
        if arr[r][c] == 0 and visited[r][c]:
            visited[r][c] = False
            fill(r, c)

for a in arr:
    print("".join(map(lambda x: str(x%10), a)))