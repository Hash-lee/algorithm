import sys

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
counts = 0
inside = list(map(int, list(sys.stdin.readline().strip())))
visit = [1 for _ in range(N)]
edge = {}

connections = sys.stdin.readlines()
for connection in connections:
    left, right = map(lambda x: int(x) - 1, connection.split())
    if inside[left] and inside[right]:
        counts += 2
        continue
    try:
        edge[left].append(right)
    except:
        edge[left] = [right]
    try:
        edge[right].append(left)
    except:
        edge[right] = [left]


def DFS(idx):
    tmp = 0
    for e in edge[idx]:
        if inside[e]:
            tmp += 1
        else:
            if visit[e]:
                visit[e] = 0
                tmp += DFS(e)
    return tmp


for idx in range(N):
    tmp = 0
    if not inside[idx] and visit[idx]:
        visit[idx] = 0
        tmp = DFS(idx)
    counts += tmp * (tmp - 1)

print(counts)
