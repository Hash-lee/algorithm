import sys
N, K = map(int, sys.stdin.readline().split())

answer = 1
for i in range(1, N+1):
    answer *= i
for j in range(1, K+1):
    answer //= j
for l in range(1, N-K+1):
    answer //= l

print(answer % 10007)