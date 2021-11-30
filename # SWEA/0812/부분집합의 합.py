import sys
sys.stdin = open('부분집합의 합.txt', 'r')


A = list(range(1,13))
T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    a = len(A)
    cnt = 0
    for i in range(1<<a):
        lst = []
        for j in range(a+1):
            if i & (1<<j):
                lst.append(A[j])
        if len(lst) == N:
            v = 0
            for l in lst:
                v += l
            if v == K:
                cnt += 1

    print('#{} {}'.format(t+1, cnt))


'''
arr = [1, 2, 3, 4]

for i in range(1<<a):
    for j in range(a+1):
        if i & (1<<j):
            print(arr[j])
'''