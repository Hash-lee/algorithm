def search(lst, n, l):
    global num
    if l == len(lst):
        if num > n and n >= B:
            num = n
    else:
        for i in range(2):
            n += lst[l] * i
            search(lst, n, l+1)

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    num = 100000000
    search(height, 0, 0)

    print('#{} {}'.format(tc ,num-B))