import sys
N = int(sys.stdin.readline())

dp = [0, 1]
for _ in range(2, N+1):
    dp[0], dp[1] = dp[1], dp[0]+dp[1]

print(dp[1])