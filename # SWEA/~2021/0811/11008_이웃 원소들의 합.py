tc = int(input())

for t in range(tc):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    for n in range(N):
        arr[n] = list(map(int, input().split()))


    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    MaxValue = -1
    MaxRow = -1
    MaxCol = -1
    for r in range(N):
        for c in range(N):
            tmpMax = 0

            for m in range(4):
                nr = r + dr[m]
                nc = c + dc[m]
                if 0 <= nr < N and 0 <= nc < N:
                    tmpMax += arr[nr][nc]

            if tmpMax > MaxValue:
                MaxValue = tmpMax
                MaxRow = r
                MaxCol = c

    print('#{} {} {} {}'.format(t+1,MaxRow,MaxCol,MaxValue))

