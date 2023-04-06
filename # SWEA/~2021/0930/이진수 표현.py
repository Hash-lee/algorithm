T = int(input())+1
    for t in range(1, T):
        N, M = map(int, input().split())

    switch = 'ON'
    for i in range(N):
        if not M&(1<<i):
            switch = 'OFF'
            break
    print('#{} {}'.format(t, switch))