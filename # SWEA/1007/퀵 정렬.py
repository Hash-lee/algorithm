def qs(lst, l, r):
    if l < r:
        s = part(lst, l, r)
        qs(lst, l, s-1)
        qs(lst, s+1, r)

def part(lst, l, r):
    p = lst[l]
    i, j = l, r
    while i <= j:
        while i <= j and lst[i] <= p: i += 1
        while i <= j and lst[j] >= p: j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
            i, j = i+1, j-1
    lst[l], lst[j] = lst[j], lst[l]
    return j

for tc in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int, input().split()))
    qs(lst, 0, len(lst)-1)
    print('#{} {}'.format(tc, lst[len(lst)//2]))