import sys
from itertools import combinations

N = int(sys.stdin.readline())

ipts = tuple(map(int, sys.stdin.readline().split()))
combs = sorted(tuple(set(((sum(s) for r in range(1, N + 1) for s in tuple(combinations(ipts, r)))))))

i = 0
for n in combs:
    i += 1
    if n != i:
        print(i)
        exit()

print(i + 1)