import sys

line1 = list(sys.stdin.readline().rstrip())
line2 = list(sys.stdin.readline().rstrip())
L1 = len(line1)
L2 = len(line2)

dp = [[0] * (L2 + 1) for _ in range(L1 + 1)]
for i in range(1, L1 + 1):
    first = line1[i - 1]
    for j in range(1, L2 + 1):
        second = line2[j - 1]
        if first == second:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[L1][L2])