import sys
sudoku = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(9)]
todo = []
for r in range(9):
    for c in range(9):
        if sudoku[r][c] == 0:
            todo.append((r, c))
def check(idx = 0):
    if idx == len(todo):
        for s in sudoku:
            print("".join(map(str, s)))
        exit()
    else:
        r, c = todo[idx]
        available = {i for i in range(1, 10)}
        for i in range(9):
            if sudoku[r][i] in available: available.remove(sudoku[r][i])
        for j in range(9):
            if sudoku[j][c] in available: available.remove(sudoku[j][c])
        for i in range(r//3 * 3, r//3 * 3 + 3):
            for j in range(c//3 * 3, c//3 * 3 + 3):
                if sudoku[i][j] in available: available.remove(sudoku[i][j])
        
        for a in sorted(available):
            sudoku[r][c] = a
            check(idx+1)
            sudoku[r][c] = 0

check()