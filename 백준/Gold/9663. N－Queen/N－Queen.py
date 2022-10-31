import sys

N = int(sys.stdin.readline())
counts = [0]
columns = [-1] * N


def Promise(my_row, try_col):
    for i in range(my_row):
        if columns[i] == try_col or abs(columns[i] - try_col) == abs(i - my_row):
            return False
    return True


def Queen(row=0):
    if row == N:
        return escape()
    else:
        for c in range(N):
            if Promise(row, c):
                columns[row] = c
                Queen(row + 1)


def escape():
    counts[0] += 1


Queen()
print(counts[0])