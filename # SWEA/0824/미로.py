T = int(input())

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

def df(arr, r, c):
    global flag
    if flag != 1:
        for k in range(4):
            nr = r + dy[k]
            nc = c + dx[k]
            if arr[nr][nc] == 2:
                flag = 1
                break
            if arr[nr][nc] == 0:
                arr[nr][nc] = -1
                df(arr, nr, nc)
    else:
        return

for t in range(1, T+1):
    N = int(input())
    miro = [[1] * (N + 2) for _ in range(N + 2)]
    # 0: 통로 1: 벽 2: 출발 3: 도착
    for n in range(1, N+1):
        sen = input()
        for m in range(1, N+1):
            miro[n][m] = int(sen[m-1])

    flag = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if miro[i][j] == 3:
                df(miro, i, j)
                break
    print('#{} {}'.format(t, flag))
