import sys

N = int(sys.stdin.readline())
left = 0
right = 1


if N < 3:
    print([0, 1, 1][N])
else:
    for iter in range(N - 1):
        left, right = right, left + right

    print(right)