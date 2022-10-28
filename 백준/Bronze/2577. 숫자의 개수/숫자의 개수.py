import sys

A, B, C = list(map(int, sys.stdin.readlines()))
n = str(A * B * C)

lst = [0] * 10
for x in n:
    lst[int(x)] += 1

for l in lst:
    print(l)