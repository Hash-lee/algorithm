import sys
sys.stdin = open('sample.txt', 'r')

def BFS(a, b):
    for i in range(1, N+1):
        if arr[a][i] == 1 and V[i] == 0:
            V[i] = b
            BFS(i, b)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        arr[s][e], arr[e][s] = 1, 1

    V = [0]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        if V[i] == 0:
            cnt += 1
            V[i] = cnt
            BFS(i, cnt)
    
    print('#{} {}'.format(tc, cnt))