import sys

N = int(sys.stdin.readline())
arr = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
min_black = [[N * N for _ in range(N)] for __ in range(N)]
min_black[0][0] = 0

Q = [0] * (1000000)
front = -1
rear = 0
Q[rear] = (0, 0, 0)
dir_r = [1, 0, -1, 0]
dir_c = [0, 1, 0, -1]
while front < rear:
    front += 1
    row, col, black = Q[front]
    for k in range(4):
        new_row = row + dir_r[k]
        new_col = col + dir_c[k]
        if 0 <= new_row < N and 0 <= new_col < N:
            new_black = black if arr[new_row][new_col] else black + 1
            if new_black < min_black[new_row][new_col]:
                min_black[new_row][new_col] = new_black
                rear += 1
                Q[rear] = (new_row, new_col, new_black)

print(min_black[N - 1][N - 1])