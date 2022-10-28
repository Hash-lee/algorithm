import sys

a, b = map(int, sys.stdin.readline().split())
lst = [a + b, a - b, a * b, a // b, a % b]
for l in lst:
    print(l)