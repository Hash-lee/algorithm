import sys
V = int(sys.stdin.readline())
tree = {i:{} for i in range(1, V+1)}
for _ in range(V):
    node, *edges = list(map(int, sys.stdin.readline().split()))
    for i in range(0, len(edges)-1, 2):
        n = edges[i]
        d = edges[i+1]
        tree[node][n] = d

visit = [1] * (V+1)
D = [0] * (V+1)
def find(n, d=0):
    e = -1
    mx = -1
    flag = 1
    for key, value in tree[n].items():
        if visit[key]:
            visit[key] = 0
            te, tmx = find(key, d+value)
            if mx < tmx: e, mx = te, tmx
            visit[key] = 1
            flag = 0
    if flag:
        return n, d
    else:
        return e, mx
mx = -1
s = 1
while True:
    visit[s] = 0
    n, d = find(s)
    visit[s] = 1
    if mx < d: mx, s = d, n
    else: break
    

print(mx)