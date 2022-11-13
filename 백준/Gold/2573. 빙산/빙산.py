import sys

R, C = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]


dir_r = [1, 0, -1, 0]
dir_c = [0, 1, 0, -1]


def melting(row, col):
    for k in range(4):
        new_row = row + dir_r[k]
        new_col = col + dir_c[k]
        if arr[row][col] and arr[new_row][new_col] == 0 and melted[row][col]:
            melted[row][col] -= 1


def BFS():
    global front, rear
    while front < rear:
        front += 1
        row, col = Q[front]
        for k in range(4):
            new_row, new_col = row + dir_r[k], col + dir_c[k]
            if arr[new_row][new_col] and visit[new_row][new_col]:
                visit[new_row][new_col] = 0
                rear += 1
                Q[rear] = (new_row, new_col)


flag = True
year = 0
while flag:
    flag = False
    Q = [0] * 10000
    front = -1
    rear = -1
    visit = [[1 for _ in range(C)] for _ in range(R)]

    island = True
    for r in range(R):
        for c in range(C):
            if arr[r][c] and visit[r][c]:
                flag = True
                if island:
                    island = False
                    visit[r][c] = 0
                    rear += 1
                    Q[rear] = (r, c)
                    BFS()
                else:
                    flag = False
                    break
    if flag:
        year += 1
        melted = [row[:] for row in arr]
        for r in range(R):
            for c in range(C):
                if arr[r][c]:
                    melting(r, c)
        arr = melted
if island:
    print(0)
else:
    print(year)
