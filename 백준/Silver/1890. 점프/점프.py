import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dir_r = [1, 0]
dir_c = [0, 1]

count = [[0] * N for _ in range(N)]
count[0][0] = 1
for row in range(N):
    for col in range(N):
        if row == N - 1 and col == N - 1:
            print(count[row][col])
            exit()
        if arr[row][col]:
            for k in range(2):
                nr = row + dir_r[k] * arr[row][col]
                nc = col + dir_c[k] * arr[row][col]
                if nr < N and nc < N:
                    count[nr][nc] += count[row][col]