import sys

N, M = map(int, sys.stdin.readline().split())

mx = 0
while mx * (mx - 1) // 2 <= N:
    mx += 1
dp = [[0xFFFF] * mx for _ in range(N)]
dp[0][0] = 0

for _ in range(M):
    dp[int(sys.stdin.readline()) - 1] = 0

for idx in range(N - 1):
    if not dp[idx]:
        continue
    for speed in range(mx):
        try:
            if 1 < speed and dp[idx + speed - 1] and dp[idx][speed] + 1 < dp[idx + speed - 1][speed - 1]:
                dp[idx + speed - 1][speed - 1] = dp[idx][speed] + 1
            if dp[idx + speed] and dp[idx][speed] + 1 < dp[idx + speed][speed]:
                dp[idx + speed][speed] = dp[idx][speed] + 1
            if dp[idx + speed + 1] and dp[idx][speed] + 1 < dp[idx + speed + 1][speed + 1]:
                dp[idx + speed + 1][speed + 1] = dp[idx][speed] + 1
        except:
            pass

mn = min(dp[-1])
if 10000 < mn:
    print(-1)
else:
    print(mn)