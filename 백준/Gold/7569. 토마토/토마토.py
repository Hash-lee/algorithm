import sys

M, N, H = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(N)] for _ in range(H)]

fresh = 0

Q = [0] * M * N * H
front = -1
rear = -1
for height in range(H):
    for length in range(N):
        arr[height][length] = list(map(int, sys.stdin.readline().split()))
        for width in range(M):
            if arr[height][length][width] == 1:
                rear += 1
                Q[rear] = (height, length, width, 0)
            elif arr[height][length][width] == 0:
                fresh += 1
dir_w = [0, 1, 0, -1, 0, 0]
dir_l = [1, 0, -1, 0, 0, 0]
dir_h = [0, 0, 0, 0, 1, -1]
days = 0
while front < rear:
    front += 1
    height, length, width, day = Q[front]
    if days < day:
        days = day
    for k in range(6):
        new_height, new_length, new_width = height + dir_h[k], length + dir_l[k], width + dir_w[k]
        if 0 <= new_height < H and 0 <= new_length < N and 0 <= new_width < M:
            if arr[new_height][new_length][new_width] == 0:
                rear += 1
                Q[rear] = (new_height, new_length, new_width, day + 1)
                arr[new_height][new_length][new_width] = day + 1
                fresh -= 1
if fresh:
    print(-1)
else:
    print(days)