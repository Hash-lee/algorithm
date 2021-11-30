def winner(mem ,dic):
    n = len(mem)
    if n == 1:
        return mem[0]
    else:
        m = (n + 1) // 2
        lwin = winner(mem[:m], dic)
        rwin = winner(mem[m:], dic)
        return rwin if dic[lwin]%3 == dic[rwin]-1 else lwin

T = int(input())
for t in range(1, T+1):
    N = int(input())
    mem = [0] * N
    dic = {}
    lst = list(map(int, input().split()))
    for i in range(1, N+1):
        mem[i-1] = i
        dic[i] = lst[i-1]
    print('#{} {}'.format(t, winner(mem, dic)))
