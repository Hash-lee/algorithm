for tc in range(1, int(input())+1):
    battery = list(map(int,input().split()))
    k = battery[1]
    idx = 1
    cnt = 0
    while k + idx < battery[0]:
        mx = -1
        tmp = 0
        for i in range(1, battery[idx]+1):
            if mx < battery[idx+i] + i:
                mx = battery[idx+i] + i
                tmp = idx + i
        idx = tmp
        k = battery[idx]
        cnt += 1
    print('#{} {}'.format(tc, cnt))