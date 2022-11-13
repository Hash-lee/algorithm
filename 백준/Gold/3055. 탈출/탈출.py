import sys

R, C = map(int, sys.stdin.readline().split())
arr = [[1 for _ in range(C)] for __ in range(R)]
visit = [[1 for _ in range(C)] for __ in range(R)]

water_Q = [0] * R * C
w_front = -1
w_rear = -1

gosm_Q = [0] * R * C
g_front = -1
g_rear = -1

finish = 0
for row in range(R):
    string = sys.stdin.readline().strip()
    for col in range(C):
        if string[col] == "*":
            arr[row][col] = 2
            visit[row][col] = 0
            w_rear += 1
            water_Q[w_rear] = (row, col)
        elif string[col] == "X":
            arr[row][col] = 0
            visit[row][col] = 0
        elif string[col] == "D":
            arr[row][col] = -1
        elif string[col] == "S":
            visit[row][col] = 0
            g_rear += 1
            gosm_Q[g_rear] = (row, col, 0)

dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]


def onetime_water(Q, front, rear):
    tmp_Q = [0] * R * C
    tmp_front = -1
    tmp_rear = -1
    while front < rear:
        front += 1
        row, col = Q[front]
        for k in range(4):
            new_row, new_col = row + dir_r[k], col + dir_c[k]
            if 0 <= new_row < R and 0 <= new_col < C:
                if arr[new_row][new_col] == 1:
                    visit[new_row][new_col] = 0
                    arr[new_row][new_col] = 2
                    tmp_rear += 1
                    tmp_Q[tmp_rear] = (new_row, new_col)
    return tmp_Q, tmp_front, tmp_rear


def ontime_gosm(Q, front, rear):
    tmp_Q = []
    tmp_front = -1
    tmp_rear = -1
    while front < rear:
        front += 1
        row, col, time = Q[front]
        for k in range(4):
            new_row, new_col = row + dir_r[k], col + dir_c[k]
            if 0 <= new_row < R and 0 <= new_col < C:
                if arr[new_row][new_col] == 1 and visit[new_row][new_col]:
                    visit[new_row][new_col] = 0
                    tmp_rear += 1
                    tmp_Q.append((new_row, new_col, time + 1))
                elif arr[new_row][new_col] == -1:
                    return [(new_row, new_col, time + 1)], tmp_front, tmp_rear
    return tmp_Q, tmp_front, tmp_rear


flag = True
while gosm_Q:
    if arr[gosm_Q[0][0]][gosm_Q[0][1]] == -1:
        finish = gosm_Q[0][2]
        flag = False
        break
    water_Q, w_front, w_rear = onetime_water(water_Q, w_front, w_rear)
    gosm_Q, g_front, g_rear = ontime_gosm(gosm_Q, g_front, g_rear)

if flag:
    print("KAKTUS")
else:
    print(finish)