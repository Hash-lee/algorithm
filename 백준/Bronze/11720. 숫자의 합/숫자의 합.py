import sys

N, num = map(int, sys.stdin.readlines())
answer = 0
for _ in range(N):
    answer += num % 10
    num = num // 10

print(answer)