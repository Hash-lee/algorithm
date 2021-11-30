import sys; sys.stdin = open('sample.txt', 'r')

dr = [0, 1]
dc = [1, 0]

def BFS(r, c):
    for k in range(2):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < N and nc < N and hap[r][c] + arr[nr][nc] < hap[nr][nc]:
            hap[nr][nc] = hap[r][c] + arr[nr][nc]
            BFS(nr, nc)



T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [0] * N
    hap = [[99999]* N for _ in range(N)]
    for n in range(N):
        arr[n] = tuple(map(int, input().split()))
    
    hap[0][0] = arr[0][0]
    BFS(0, 0)

    print('#{} {}'.format(tc, hap[N-1][N-1]))