import sys
sys.stdin = open('sample4.txt', 'r')


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = [0] * N

    for n in range(N):
        in_str = input()
        arr[n] = in_str

    print('#'+str(tc+1), end= ' ')
    for i in range(N):
        for j in range(N-M+1):
            tmp1, tmp2 = '1', '2'
            if arr[i][j] == arr[i][j+M-1]:
                tmp1, tmp2 = '', ''
                for k in range(M):
                    tmp1 += arr[i][j+k]
                    tmp2 += arr[i][j+M-k-1]
            if tmp1 == tmp2:
                print(tmp1)

    for i in range(N-M+1):
        for j in range(N):
            tmp1, tmp2 = '1', '2'
            if arr[i][j] == arr[i + M-1][j]:
                tmp1, tmp2 = '', ''
                for k in range(M):
                    tmp1 += arr[i+k][j]
                    tmp2 += arr[i+M-k-1][j]
            if tmp1 == tmp2:
                print(tmp1)