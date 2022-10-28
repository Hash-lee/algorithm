import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

result = []
for a in A:
    if a < X:
        result.append(a)
print(" ".join(list(map(str, result))))