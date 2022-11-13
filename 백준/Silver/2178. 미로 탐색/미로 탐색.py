import sys

R, C = map(int, sys.stdin.readline().split())

arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(R)]

visit = [[1] * C for _ in range(R)]
visit[0][0] = 0

Q = [0] * (R * C)
front = -1
rear = 0
Q[rear] = (0, 0)


dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]
while front < rear and arr[R - 1][C - 1] == 1:
    front += 1
    row, col = Q[front]
    for k in range(4):
        new_row = row + dir_r[k]
        new_col = col + dir_c[k]
        if 0 <= new_col < C and 0 <= new_row < R:
            if arr[new_row][new_col] and visit[new_row][new_col]:
                visit[new_row][new_col] = 0
                rear += 1
                Q[rear] = (new_row, new_col)
                arr[new_row][new_col] = arr[row][col] + 1

print(arr[R - 1][C - 1])