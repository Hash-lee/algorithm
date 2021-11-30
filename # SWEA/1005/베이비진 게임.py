T = int(input())
for t in range(1, T+1):
    cards = list(map(int, input().split()))
    p1 = [0] * 11
    p2 = [0] * 11

    
    for i in range(12):
        flag1 = 0
        if i % 2: p2[cards[i]] += 1
        else: p1[cards[i]] += 1

        flag2 = 0
        if i>=4:
            for j in range(1,10):
                if p1[j] == 3 or (p1[j-1] and p1[j] and p1[j+1]):
                    print('#{} {}'.format(t, 1))
                    flag2 = 1
                    break
                elif p2[j] == 3 or (p2[j-1] and p2[j] and p2[j+1]):
                    print('#{} {}'.format(t, 2))
                    flag2 = 1
                    break
        if flag2: break
        flag1 = 1
    if flag1: print('#{} {}'.format(t, 0))