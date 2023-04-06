n = int(input())
for i in range(n):
    k = int(input())
    l = list(map(int, input().split()))
    drop = 0
    for x in range(len(l)-1):
        d = 0
        for y in range(x+1, len(l)):
            if l[x] > l[y] :
                d += 1
        if d > drop:
            drop = d
    print('#{0} {1}'.format(i+1, drop))