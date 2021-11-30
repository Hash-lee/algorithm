T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    Mx = 0
    mx = 10000000
    
    for j in range(N-M+1):
        tmp = 0
        for k in range(M):
            tmp += numbers[j+k]
        if tmp > Mx:
            Mx = tmp
        if tmp < mx:
            mx = tmp
    r = Mx - mx
    
    print('#{} {}'.format(i+1, r))