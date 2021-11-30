import sys
sys.stdin = open('s4.txt', 'r')


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [0] * 401
    mx = 0

    for n in range(N):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a

        if b%2:
            b += 1
        elif a%2 == 0:
            a -= 1
        for i in range(a, b+1):
            arr[i] += 1
            if arr[i] > mx:
                mx = arr[i]
    print('#{} {}'.format(t, mx))