T = int(input())

for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    arr = [0] * len(nums)
    Idx = 0
    for num in nums:
        if num == 0:
            Idx -= 1
            arr[Idx] = num
        else:
            arr[Idx] = num
            Idx += 1

    x = 0
    for a in arr:
        x += a
    print('#{} {}'.format(t, x))





    '''
    for num in nums:
        if num == 0:
            arr.pop()
        else:
            arr.append(num)
    '''