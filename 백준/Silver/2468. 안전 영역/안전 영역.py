import sys
sys.setrecursionlimit(10**5)


N = int(sys.stdin.readline())
arr = [list(map(int, n.split())) for n in sys.stdin.readlines()]
V = [[1 for _ in range(N)] for _ in range(N)]


mn = 0xFF
mx = -1

dir_x = [-1, 0, 1, 0]
dir_y = [0, 1, 0, -1]


def BFS(r, c, rain):
    for k in range(4):
        dx = dir_x[k]
        dy = dir_y[k]
        nr, nc = r + dy, c + dx
        if 0 <= nr < N and 0 <= nc < N:
            if V[nr][nc] and arr[nr][nc] > rain:
                V[nr][nc] = 0
                BFS(nr, nc, rain)


lst = set([])
for r in range(N):
    for c in range(N):
        lst.add(arr[r][c])
lst = list(set(lst))

island = 1
for rain in lst:
    V = [[1 for _ in range(N)] for _ in range(N)]
    som = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] > rain and V[r][c]:
                V[r][c] = 0
                som += 1
                BFS(r, c, rain)
    if som > island:
        island = som

print(island)