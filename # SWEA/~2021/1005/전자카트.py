import sys; sys.stdin = open('sample.txt', 'r')

T = int(input())

def np(a, b, arr):
    if b == 0:
        nums.append([1]+ arr + [1])
    for i in range(2, a+1):
        if not i in arr: np(a, b-1, arr +[i])

for tc in range(1, T+1):
    N = int(input())
    price = [0] * (N + 1)
    for n in range(1, N + 1):
        price[n] = [0] + list(map(int, input().split()))

    nums = []
    np(N, N-1, [])

    answer = 50000
    for num in nums:
        p = 0
        for i in range(N):
            p += price[num[i]][num[i+1]]
            if p > answer: break
        if p < answer: answer = p

    print('#'+str(tc), str(answer))
    
