import sys

T = sys.stdin.readline()
for tc in range(int(T)):
    result = sys.stdin.readline()
    ser = 1
    score = 0

    for r in result:
        if r == "O":
            score += ser
            ser += 1
        else:
            ser = 1

    print(score)