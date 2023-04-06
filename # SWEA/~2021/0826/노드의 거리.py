import sys
sys.stdin = open('sample2.txt', 'r')

def push(item):
    global r
    Q[r] = item
    r = r + 1

def my_pop():
    global f
    f = f + 1
    if f != r: return Q[f]

def isEmpty():
    global f, r
    return f+1 == r

def bfs(s, g):
    for i in range(1, V+1):
        if arr[s][i] == 1 and visited[i] == 0:
            push(i)
            visited[i] = visited[s] + 1
    while not isEmpty():
        bfs(my_pop(), g)



T = int(input())
for t in range (1, T+1):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        r, c = map(int, input().split())
        arr[r][c] = arr[c][r] = 1

    S, G = map(int, input().split())

    visited = [0] * (V+1)

    Q = [0] * (V+1)
    f = -1
    r = 0
    bfs(S, G)

    print('#{} {}'.format(t,visited[G]))
