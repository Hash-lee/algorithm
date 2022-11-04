import sys

A, B, C = map(int, sys.stdin.readline().split())


def divide(A, B, C):
    if B == 1:
        return A % C
    elif B == 2:
        return (A**2) % C
    elif B % 2:
        return (divide(A, B - 1, C) * A) % C
    else:
        return (divide(A, B // 2, C) ** 2) % C


print(divide(A, B, C))