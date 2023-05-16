import sys
N = int(sys.stdin.readline()) % 1500000
dp = [0, 1]
for _ in range(2, N+1):
    dp[0], dp[1] = dp[1], (dp[0]+dp[1])%1000000

print(dp[1])