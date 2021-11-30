import sys
sys.stdin = open('sample.txt', 'r')

def fs(x):
    if x != V[x]:
        x = fs(V[x])
    return V[x]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    V = list(range(N+1))
    answer = N
    for _ in range(M):
        s, e = map(int, input().split())
        a = fs(s)
        b = fs(e)
        if a == b: continue
        V[b] = a
        answer -= 1

    print('#{} {}'.format(tc, answer))
    
