for t in range(1, int(input())+1):
    N = int(input())
    se = [0] * N
    for n in range(N):
        se[n] = tuple(map(int, input().split()))
    se.sort()

    flag = 1
    while flag:
        l = len(se)
        mx = [0] * l
        for i in range(l):
            for j in range(l):
                if i != j:
                    if se[i][0] <= se[j][0] < se[i][1]:
                        mx[i] += 1
                        mx[j] += 1
        k = max(mx)
        if k == 0:
            flag = 0
            print('#{} {}'.format(t, l))
        else:
            se.pop(mx.index(k))