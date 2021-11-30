def ES(arr, k):
    db.append((arr, k))
    n = len(arr)
    if k == 0:
        c = 0
        for i in range(n):
            c += arr[i] * (10**(n-i-1))
        if not c in nums:
            nums.append(c)
    else:
        for i in range(n-1):
            for j in range(i+1,n):
                crr = arr[:]
                crr[i], crr[j] = crr[j], crr[i]
                if not (crr, k-1) in db:
                    ES(crr, k-1)

T = int(input())
for t in range(1, T+1):
    N, M = input().split()
    M = int(M)
    N = list(map(int ,(" ".join(N)).split()))
    
    nums = []
    db = []
    ES(N, M)
    
    answer = 0
    for num in nums:
        if num > answer:
            answer = num
    print('#{} {}'.format(t, answer))