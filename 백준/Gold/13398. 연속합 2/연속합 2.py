import sys

N = int(sys.stdin.readline())
blank = []
nums = list(map(int, sys.stdin.readline().split()))
blank.append(nums[0])

for idx in range(1, N):
    if nums[idx] < 0 or blank[-1] < 0:
        blank.append(nums[idx])
    else:
        blank[-1] += nums[idx]

if max(blank) <= 0:
    print(max(blank))
    exit()


L = len(blank)
dp = [[0, 0] for _ in range(L + 1)]

mx = -1
for idx in range(1, L + 1):
    dp[idx][0] = max(dp[idx - 1][0] + blank[idx - 1], blank[idx - 1])
    dp[idx][1] = max(dp[idx - 1][0], dp[idx - 1][1] + blank[idx - 1])


for idx in range(1, L + 1):
    for j in range(2):
        if mx < dp[idx][j]:
            mx = dp[idx][j]

print(mx)