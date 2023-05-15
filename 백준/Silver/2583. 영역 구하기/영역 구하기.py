import sys
sys.setrecursionlimit(10**6)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(r, c, cnt):
    arr[r][c] = cnt
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0<=nr<M and 0<=nc<N:
            if arr[nr][nc] == 0:
                BFS(nr, nc, cnt)

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            arr[r][c] = -1

cnt = 0
for r in range(M):
    for c in range(N):
        if arr[r][c] == 0:
            cnt += 1
            BFS(r,c,cnt)

print(cnt)
num = [0]*(cnt+1)
for i in range(1, cnt+1):
    for r in range(M):
        for c in range(N):
            if arr[r][c] == i: num[i] +=1
num.sort()
for i in range(1, cnt+1):
    print(num[i], end = ' ')