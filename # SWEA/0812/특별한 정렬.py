import sys
sys.stdin = open('특별한 정렬.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N):
        if i % 2:
            mx = 1000
            mxj = -1
            for j in range(i, N):
                if numbers[j] < mx:
                    mxj = j
                    mx = numbers[j]
            if mxj != -1:
                numbers[mxj] = numbers[i]
                numbers[i] = mx
        else:
            Mx = 0
            Mxj = -1
            for j in range(i, N):
                if numbers[j] > Mx:
                    Mxj = j
                    Mx = numbers[j]
            if Mxj != -1:
                numbers[Mxj] = numbers[i]
                numbers[i] = Mx

    print('#{} {}'.format(t+1," ".join(list(map(str, numbers[:10])))))