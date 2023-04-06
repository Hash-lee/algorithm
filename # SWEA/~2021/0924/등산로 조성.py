import sys
sys.stdin = open('등산로 조성.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def line(r, c, n, k, m):
    for i in range(4):
        arr[r][c] = n
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<= nr < N and 0 <= nc < N:
            if  arr[nr][nc] == 0 and cm[nr][nc] - k < m:
                if cm[nr][nc] >= cm[r][c]:
                    line(nr, nc, n+1, 0, cm[r][c]-1)
                else:
                    line(nr, nc, n+1, k, cm[nr][nc])
    arr[r][c] = 0
    global answer
    if answer < n: answer = n

T = int(input())
for t in range(1, T+1):
    answer = 0
    N, K = map(int, input().split())
    mountain = [0] * N
    for n in range(N):
        mountain[n] = list(map(int, input().split()))
    mx = 0
    for m in mountain:
        for n in m:
            if n > mx:
                mx = n

    
    for r in range(N):
        for c in range(N):
            if mountain[r][c] == mx:
                cm = mountain[:]
                arr = [[0] * N for _ in range(N)]
                line(r, c, 1, K, mx)
    
    print('#{} {}'.format(t, answer))