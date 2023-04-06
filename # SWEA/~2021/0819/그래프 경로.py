import sys
sys.stdin = open('그래프 경로.txt', 'r')

T = int(input())

def dfs(v):
    visited[v] = 1
    for w in range(1, V+1):
        if arr[v][w] == 1 and visited[w] != 1:
            dfs(w)


for t in range(1, T+1):
    V, E = map(int, input().split())
    visited = [0] * (V+1)
    arr = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        s, e = map(int, input().split())
        # 주의 - 방향성 그래프
        arr[s][e] = 1

    v, w = map(int, input().split())

    dfs(v)
    if visited[w]:
        print('#{} {}'.format(t, 1))
    else: print('#{} {}'.format(t, 0))