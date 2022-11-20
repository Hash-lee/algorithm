import sys

T = int(sys.stdin.readline())
for tc in range(T):
    N = int(sys.stdin.readline())
    grades = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    grades.sort()
    success = 1
    cutline = grades[0][1]
    for idx in range(1, N):
        if grades[idx][1] < cutline:
            success += 1
            cutline = grades[idx][1]

    print(success)