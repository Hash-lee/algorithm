t = int(input())
for case in range(t):
    n, q = map(int, input().split())
    box = ['0'] * n
    for i in range(1, q+1):
        l, r = map(int, input().split())
        for k in range(l, r+1):
            box[k-1] = str(i)
    
    print('#{} {}'.format(case+1, " ".join(box)))

    #실행시간 개선 필요