import sys
sys.stdin = open('sample.txt', 'r')

def dj1(n):
    v1[n] = 1
    mn = 0xffff
    idx = -1
    for i in range(1,N+1):
        if v1[i] == 0 and arr[i][n]:
            if d1[i] > d1[n] + arr[i][n]:
                d1[i] = d1[n] + arr[i][n]
        if mn > d1[i] and v1[i] == 0:
            mn = d1[i]
            idx = i
    return idx

def dj2(n):
    v2[n] = 1
    mn = 0xffff
    idx = -1
    for i in range(1,N+1):
        if v2[i] == 0 and arr[n][i]:
            if d2[i] > d2[n] + arr[n][i]:
                d2[i] = d2[n] + arr[n][i]
        if mn > d2[i] and v2[i] == 0:
            mn = d2[i]
            idx = i
    return idx

for tc in range(1, int(input())+1):
    N, M, X = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    
    for _ in range(M):
        x, y, c = map(int, input().split())
        arr[x][y] = c

    d1 = [0xfffff] * (N+1)
    v1 = [0] * (N+1)
    d1[X] = 0
    n = X
    while n != -1:
        n = dj1(n)

    d2 = [0xfffff] * (N+1)
    v2 = [0] * (N+1)
    d2[X] = 0
    m = X
    while m != -1:
        m = dj2(m)
    
    answer = -1
    for i in range(1, N+1):
        if answer < d1[i] + d2[i]:
            answer = d1[i] + d2[i]

    print('#{} {}'.format(tc, answer))