import sys
sys.stdin = open('sample.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def supply(r, c):
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if V[r][c] + arr[nr][nc] < V[nr][nc]:
                V[nr][nc] = V[r][c] + arr[nr][nc]
                global rear
                rear += 1
                Q[rear] = (nr, nc)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [tuple(map(int, (":".join(input())).split(":"))) for _ in range(N)]
    V = [[0xffff]*N for _ in range(N)]
    V[0][0] = 0

    Q = [0] * N * N * 100
    front = -1
    rear = 0
    Q[rear] = (0,0)

    while front != rear:
        front += 1
        supply(Q[front][0], Q[front][1])
    
    print('#{} {}'.format(tc, V[N-1][N-1]))