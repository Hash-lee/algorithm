import sys
sys.stdin = open('파리퇴치.txt', 'r')


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [0] * N

    for n in range(N):
        tmp_list = list(map(int, input().split()))
        arr[n] = tmp_list

    Mv = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):

            tmp_value = 0
            for y in range(i, i + M):
                for x in range(j, j + M):
                    tmp_value += arr[y][x]
            if tmp_value > Mv:
                Mv = tmp_value



    print('#{} {}'.format(t+1, Mv))