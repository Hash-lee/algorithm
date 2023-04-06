for i in range(10):
    limit = int(input())
    lst_height = list(map(int, input().split()))
    for k in range(limit+1):
        # a: max height, b: min height
        a = 0
        idxa = 0
        b = 101
        idxb = 0
        for j in range(100):
            if lst_height[j] > a:
                a = lst_height[j]
                idxa = j
            if lst_height[j] < b:
                b = lst_height[j]
                idxb = j
        d = a - b
        lst_height[idxa] -= 1
        lst_height[idxb] += 1

    print('#{0} {1}'.format(i+1, d))