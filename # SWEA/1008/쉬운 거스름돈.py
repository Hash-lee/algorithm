pay = {1: 50000, 2:10000, 3:5000, 4:1000, 5:500, 6:100, 7:50, 8:10}

T = int(input())
for t in range(1, T+1):
    p = int(input())
    cnt = [0]*8
    i = 1
    while p >= 10:
        while p >= pay[i]:
            cnt[i-1] += 1
            p -= pay[i]
        i += 1
    print('#{}'.format(t))
    print(" ".join(map(str, cnt)))