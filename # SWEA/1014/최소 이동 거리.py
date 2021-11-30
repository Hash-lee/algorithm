import sys
sys.stdin = open('sample.txt', 'r')

def DFS(s):
    for e, p in D[s]:
        if V[e] > V[s] + p:
            V[e] = V[s] + p
            DFS(e)

for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    D = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, p = map(int, input().split())
        D[s].append((e, p))
    V = [99999999] *(N+1)

    V[0] = 0
    DFS(0)

    print('#{} {}'.format(tc, V[N]))