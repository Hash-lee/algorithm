import sys

R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(R)]
visit = [[1 for _ in range(C)] for _ in range(R)]


def garo(row, col):
    if col + 1 < C and arr[row][col + 1] == "-":
        visit[row][col + 1] = 0
        garo(row, col + 1)


def sero(row, col):
    if row + 1 < R and arr[row + 1][col] == "|":
        visit[row + 1][col] = 0
        sero(row + 1, col)


plate = 0
for row in range(R):
    for col in range(C):
        if visit[row][col]:
            visit[row][col] = 0
            if arr[row][col] == "-":
                plate += 1
                garo(row, col)
            else:
                plate += 1
                sero(row, col)

print(plate)