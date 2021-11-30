import sys
sys.stdin = open('sample.txt', 'r')


dr = [0 , 1, 0, -1]
dc = [1, 0, -1, 0]
def BFS(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            h = arr[nr][nc] - arr[r][c]             # 이렇게 할 필요 없는 이유: 어차피 우하단 이동,
            if h < 0: h = 0                         # 특정 높이로 이동하는 것은 왼쪽에서 오던 위에서 오던 같음
            if p[nr][nc] == 0 or p[nr][nc] > p[r][c] + h + 1:
                p[nr][nc] = p[r][c] + h + 1
                global rear
                rear += 1
                Q[rear] = (nr, nc)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    p = [[0]*N for _ in range(N)]
    
    Q = [0]*N*N*N
    front = -1
    rear = 0
    Q[rear] = (0, 0)
    while front != rear:
        front += 1
        BFS(Q[front][0], Q[front][1])
    print('#{} {}'.format(tc, p[N-1][N-1]))

