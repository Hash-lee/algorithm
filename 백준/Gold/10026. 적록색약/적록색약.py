import sys
sys.setrecursionlimit(10**6)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

N = int(input())
arr1 = [0] * N
arr2 = [[0] * N for _ in range(N)]

def BFS(arr, N, y, x, c, n):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0<= nx < N and arr[ny][nx] == c:
            arr[ny][nx] = n
            BFS(arr, N, ny, nx, c, n)

for n in range(N):
    arr1[n] = (":".join(input())).split(":")

for r in range(N):
    for c in range(N):
        if arr1[r][c] == 'R':
            arr2[r][c] = -1
            arr1[r][c] = -1
        elif arr1[r][c] == 'G':
            arr2[r][c] = -1
            arr1[r][c] = -2
        elif arr1[r][c] == 'B':
            arr2[r][c] = -2
            arr1[r][c] = -3

n1 = n2 = 0
for y in range(N):
    for x in range(N):
        if arr1[y][x] == -1 or arr1[y][x] == -2 or arr1[y][x] == -3:
            n1 += 1
            BFS(arr1, N, y, x, arr1[y][x], n1)
        
        if arr2[y][x] == -1 or arr2[y][x] == -2:
            n2 += 1
            BFS(arr2, N, y, x, arr2[y][x], n2)

print(n1, n2)