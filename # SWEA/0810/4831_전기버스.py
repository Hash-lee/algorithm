T = int(input())

for i in range(T):
    #k: 최대 이동 거리 n: 종점, m: 충전기 위치
    k, n, m = map(int, input().split())
    charger = list(map(int,input().split()))
    #now: 현재 위치 cnt: 충전 횟수
    stn = list(range(n))
    now = 0
    cnt = 0
    while now < n - k:
        nxt = 0
        #다음 충전소 찾기
        for j in range(k):
            if stn[now+k-j] in charger:
                nxt = now + k - j
                now = nxt
                cnt += 1
                break
        #거리 내에 충전소 없을 시
        if nxt == 0:
            cnt = 0
            break
    print('#{} {}'.format(i+1, cnt))