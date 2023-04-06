import sys
sys.stdin = open('이진탐색.txt', 'r')


T = int(input())

def tree(n):
    global N, cnt
    if n * 2 <= N:
        tree(n * 2)
    arr[n] = cnt
    cnt += 1
    if n * 2 + 1 <= N:
        tree(n * 2 + 1)

for t in range(1, T+1):
    N = int(input())
    cnt = 1
    arr = [0] * (N+1)
    tree(1)
    print('#{} {} {}'.format(t, arr[1], arr[N//2]))

