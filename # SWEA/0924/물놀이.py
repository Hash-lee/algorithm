import sys
sys.stdin = open('물놀이.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Q = [0] * N * M
    front = -1
    rear = -1
    answer = 0
    
    arr = [[-1] * M for _ in range(N)]
    sen = [0] * N
    for i in range(N):
        sen[i] = input()
        for j in range(M):
            if sen[i][j] == 'W':
                rear += 1
                Q[rear] = (i, j)
                arr[i][j] = 0
    
    while front != rear:
        front += 1
        r = Q[front][0]
        c = Q[front][1]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if sen[nr][nc] == 'L' and arr[nr][nc] == -1:
                    rear += 1
                    Q[rear] = (nr, nc)
                    arr[nr][nc] = arr[r][c] + 1
                    answer += arr[r][c] + 1
    print('#{} {}'.format(t, answer))
    