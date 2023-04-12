import sys

N = int(sys.stdin.readline())
X = [0] * N
for i in range(N):
    X[i] = tuple(map(int, sys.stdin.readline().split()))

X.sort()
total = sum(map(lambda x: x[1], X))
people = 0
idx = -1
while people < total / 2:
    idx += 1
    people += X[idx][1]

print(X[idx][0])