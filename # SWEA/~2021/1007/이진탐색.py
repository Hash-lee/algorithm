def find(lst, l, r, x):
    m = (l+r)//2
    if r < l or (l == r and lst[m] != x): return 0
    if lst[m] == x: return 1
    elif lst[m] > x:
        chk.append('L')
        return find(lst, l, m-1, x)
    elif lst[m] < x:
        chk.append('R')
        return find(lst, m+1, r, x)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()

    answer = 0
    for b in B:
        chk = []
        if find(A, 0, N-1, b):
            cnt = 1
            if chk:
                for i in range(1, len(chk)):
                    if chk[i] == chk[i-1]: cnt = 0
            if cnt: answer += 1
    
    print('#{} {}'.format(tc, answer))

