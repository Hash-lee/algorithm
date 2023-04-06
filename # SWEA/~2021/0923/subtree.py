import sys
sys.stdin = open('subtree.txt', 'r')

def sub(a):
    for n in range(len(arr[a])):
        if arr[a][n] == 1:
            global cnt
            cnt += 1
            sub(n)

T = int(input())

for t in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    visited = [0] * (E + 2)
    cnt = 1
    arr = [[0] * (E + 2) for _ in range(E + 2)]
    for i in range(E):
        arr[edges[2*i]][edges[2*i+1]] = 1
    sub(N)

    print('#{} {}'.format(t, cnt))