dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def CLN(r, c, d):
    global cnt
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1
    for x in range(1,5):
        k = (d+4-x)%4
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 0:
            return CLN(nr, nc, k)
    nr = r - dr[d]
    nc = c - dc[d]
    if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 2:
        CLN(nr, nc, d)

M, N = map(int, input().split())
R, C, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
cnt = 0
CLN(R, C, D)
print(cnt)