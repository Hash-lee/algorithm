import sys
sys.stdin = open('길찾기.txt', 'r')

def dfs(v):
    visited[v] = 1
    for w in range(100):
        if arr[v][w] == 1 and visited[w] != 1:
            dfs(w)

for _ in range(10):
    t, E = map(int, input().split())
    road = list(map(int, input().split()))
    visited = [0] * 100
    arr = [[0] * 100 for _ in range(100)]

    for i in range(E):
        arr[road[i*2]][road[i*2 + 1]] = 1

    dfs(0)
    print('#{} {}'.format(t, visited[99]))