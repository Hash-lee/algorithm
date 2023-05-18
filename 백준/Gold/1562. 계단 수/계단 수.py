import sys

N = int(sys.stdin.readline())
mx = 1000000000
if N < 10:
    print(0)
    exit()

dp = [[[0] * 1024 for _ in range(11)] for _ in range(N)]
for i in range(1, 10):
    dp[0][i][1 << i] = 1

for i in range(1, N):
    for j in range(10):
        for k in range(1024):
            dp[i][j][k | 1 << j] += (dp[i-1][j-1][k] + dp[i-1][j+1][k]) % mx

print(sum(map(lambda x: x[1023], dp[-1])) % mx)
