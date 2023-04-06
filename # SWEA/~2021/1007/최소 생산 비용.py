def com(n, m):
    global M
    if n == 0:
            if m < M:M = m
    else:
        if m > M: pass
        else:
            for i in range(N):
                if visited[i] == 0:
                    visited[i] = 1
                    m += arr[n-1][i]
                    if m < M: com(n-1, m)
                    m -= arr[n-1][i]
                    visited[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [0] * N
    for n in range(N):
        arr[n] = tuple(map(int,input().split()))
    
    M = 1500
    visited = [0] * N
    com(N, 0)
    print('#{} {}'.format(tc, M))