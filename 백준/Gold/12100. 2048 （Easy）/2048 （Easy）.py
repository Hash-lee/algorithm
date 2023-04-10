import sys

N = int(sys.stdin.readline())
origin = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def left(arr):
    for r in range(N):
        fill = 1
        for c in range(1, N):
            if arr[r][c]:
                if arr[r][fill - 1] == 0:
                    arr[r][fill - 1] = arr[r][c]
                    arr[r][c] = 0
                else:
                    if arr[r][fill - 1] == arr[r][c]:
                        arr[r][fill - 1] *= 2
                        arr[r][c] = 0
                    else:
                        arr[r][fill] = arr[r][c]
                        if fill != c:
                            arr[r][c] = 0
                    fill += 1
    return arr


def right(arr):
    for r in range(N):
        fill = N - 2
        for c in range(N - 2, -1, -1):
            if arr[r][c]:
                if arr[r][fill + 1] == 0:
                    arr[r][fill + 1] = arr[r][c]
                    arr[r][c] = 0
                else:
                    if arr[r][fill + 1] == arr[r][c]:
                        arr[r][fill + 1] *= 2
                        arr[r][c] = 0
                    else:
                        arr[r][fill] = arr[r][c]
                        if fill != c:
                            arr[r][c] = 0
                    fill -= 1
    return arr


def up(arr):
    for c in range(N):
        fill = 1
        for r in range(1, N):
            if arr[r][c]:
                if arr[fill - 1][c] == 0:
                    arr[fill - 1][c] = arr[r][c]
                    arr[r][c] = 0
                else:
                    if arr[fill - 1][c] == arr[r][c]:
                        arr[fill - 1][c] *= 2
                        arr[r][c] = 0
                    else:
                        arr[fill][c] = arr[r][c]
                        if fill != r:
                            arr[r][c] = 0
                    fill += 1
    return arr


def down(arr):
    for c in range(N):
        fill = N - 2
        for r in range(N - 2, -1, -1):
            if arr[r][c]:
                if arr[fill + 1][c] == 0:
                    arr[fill + 1][c] = arr[r][c]
                    arr[r][c] = 0
                else:
                    if arr[fill + 1][c] == arr[r][c]:
                        arr[fill + 1][c] *= 2
                        arr[r][c] = 0
                    else:
                        arr[fill][c] = arr[r][c]
                        if fill != r:
                            arr[r][c] = 0
                    fill -= 1
    return arr


answer = -1


def check(origin, n=0):
    if n == 5:
        global answer
        answer = max(answer, max(map(max, origin)))
    else:
        for i in range(4):
            if i == 0:
                check(up([line[:] for line in origin]), n + 1)
            if i == 1:
                check(down([line[:] for line in origin]), n + 1)
            if i == 2:
                check(left([line[:] for line in origin]), n + 1)
            if i == 3:
                check(right([line[:] for line in origin]), n + 1)


check(origin)
print(answer)