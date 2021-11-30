import sys
sys.stdin = open('sample.txt', 'r')

T = int(input())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if arr[ny][nx] == visited[ny][nx]:
                visited[ny][nx] = visited[y][x] - 1
                Q.append([ny, nx])
            elif arr[ny][nx] == 3:
                global result
                result = -visited[y][x]
                break

for t in range(1, T+1):
    N = int(input())
    Q = []
    visited = [[0] * N for _ in range(N)]
    arr = [[0] * N for _ in range(N)]
    for y in range(N):
        sen = input()
        for x in range(N):
            arr[y][x] = int(sen[x])
            if sen[x] == '2':
                sy, sx = y, x

    result = 0
    bfs(sy, sx)
    while Q:
        tmp = Q.pop(0)
        bfs(tmp[0], tmp[1])

    print('#{} {}'.format(t, result))