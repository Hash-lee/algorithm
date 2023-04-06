import sys
sys.stdin = open('s5.txt', 'r')


T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [[0] * (N+2) for _ in range(N+2)]
    for n in range(N):
        sen = list(map(int, input().split()))
        for s in range(N):
            arr[n+1][s+1] = sen[s]

    result = 0

    for r in range(1, N+1):
        for c in range(1, N - K + 2):
            flag = 0
            if arr[r][c-1] == 0 and arr[r][c + K] == 0:
                flag = 1
                for k in range(c, c + K):
                    if arr[r][k] != 1:
                        flag = 0
                if flag == 1:
                    result += 1

    for c in range(1, N+1):
        for r in range(1, N - K + 2):
            flag = 0
            if arr[r-1][c] == 0 and arr[r+K][c] == 0:
                flag = 1
                for k in range(r, r + K):
                    if arr[k][c] != 1:
                        flag = 0
                if flag == 1:
                    result += 1
    print('#{} {}'.format(t, result))