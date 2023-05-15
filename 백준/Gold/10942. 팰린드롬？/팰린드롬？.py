import sys
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

arr = [[0] * N for _ in range(N)]
visit = [[1] * N for _ in range(N)]

def mark(l, r):
    if l <= r and visit[l][r]:
        visit[l][r] = 0
        if numbers[l] == numbers[r]:
           arr[l][r] = mark(l+1, r-1)
    if l > r: return 1
    return arr[l][r]

for _ in range(M):
    S, E = map(lambda x:int(x)-1, list(map(int, sys.stdin.readline().split())))
    print(arr[S][E] if not visit[S][E] else mark(S, E))