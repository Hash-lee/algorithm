import sys
sys.stdin = open('s8.txt', 'r')


T = int(input())

for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    mx = 0
    result = 0
    for i in range(-1, -N - 1, -1):
        lst[i] -= mx
        if lst[i] < 0:
            result -= lst[i]
        else:
            mx += lst[i]

    print('#{} {}'.format(t, result))