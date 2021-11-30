dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def SEARCH(r, c):
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == arr[r][c] + 1:
            return SEARCH(nr, nc) + 1
    return 1

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    mx = 0
    num = [[0] * N for _ in range(N)]
    room = 0

    for i in range(N):
        for j in range(N):
            num[i][j] = SEARCH(i, j)
            if num[i][j] > mx:
                room = arr[i][j]
                mx = num[i][j]
            if num[i][j] == mx and room > arr[i][j]:
                room = arr[i][j]

    print('#{} {} {}'.format(tc, room, mx))