# t=테스트 넘버 n=입력개수 h=건물 높이 x=결과
t = 1
while t <=10:
    n = int(input())
    h = list(map(int, input().split()))
    x = 0
    for i in range(2, n-2):
        l = [h[i-2], h[i-1], h[i+1], h[i+2]]
        v = 0
        for k in l:
            if k > v:
                v = k
        if h[i] > v:
            x += (h[i] - v)
    print('#{0} {1}'.format(t, x))
    t += 1