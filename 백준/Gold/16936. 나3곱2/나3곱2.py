import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


def count(number):
    lst = [0, 0]
    while not number % 3:
        number //= 3
        lst[0] -= 1

    while not number % 2:
        number //= 2
        lst[1] += 1
    return lst[0], lst[1]


arr = sorted(arr, key=lambda x: count(x))
print(" ".join(map(str, arr)))