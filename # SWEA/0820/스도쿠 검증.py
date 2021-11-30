import sys
sys.stdin = open('s6.txt', 'r')


T = int(input())


def sudoku(arr):
    rev = [[0] * 9 for _ in range(9)]

    for r in range(9):
        for c in range(9):
            rev[r][c] = arr[c][r]

    for r in range(9):
        for c in range(9):
            if not (c+1) in arr[r]:
                return 0

    for r in range(9):
        for c in range(9):
            if not (c+1) in rev[r]:
                return 0

    for r in range(0,9,3):
        for c in range(0,9,3):
            tmp = []
            for y in range(r, r+3):
                for x in range(c, c+3):
                    tmp += [arr[y][x]]
            for k in range(1, 10):
                if not k in tmp:
                    return 0
    return 1



for t in range(1, T+1):
    arr = [0] * 9
    for i in range(9):
        arr[i] = list(map(int, input().split()))
    print('#{} {}'.format(t, sudoku(arr)))