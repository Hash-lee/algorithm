import sys
sys.stdin = open('sample.txt', 'r')

def tree(u):
    t[u] = 1
    for v, w in G[u]:
        if t[v] == 0 and s[v] > w:
            p[v] = u
            s[v] = w

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for e in range(E):
        n1, n2, w = map(int,input().split())
        G[n1].append((n2, w))
        G[n2].append((n1, w))

    t = [0] * (V+1)
    p = [None] * (V+1)
    s = [99] * (V+1)
    s[0] = 0
    tree(0)

    answer = 0
    cnt = 0
    while cnt < V:
        u, mn = 0, 99
        for i in range(V+1):
            if t[i] != 1 and s[i] < mn:
                u, mn = i, s[i]
        answer += s[u]
        tree(u)
        cnt += 1
    print('#{} {}'.format(tc, answer))