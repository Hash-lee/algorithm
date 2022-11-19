import sys

N = int(sys.stdin.readline())

arraies = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]


dp = [[0] * N for _ in range(N + 1)]

for i in range(N - 1):
    dp[i][i + 1] = arraies[i][0] * arraies[i][1] * arraies[i + 1][1]


def check(i, j):
    # 2~3 + 4~5 = 2~5
    mn = 2**31
    for k in range(i, j):
        tmp = dp[i][k] + dp[k + 1][j] + (arraies[i][0] * arraies[k][1] * arraies[j][1])
        if tmp < mn:
            mn = tmp
    return mn


for end in range(2, N):
    for next in range(N - end):
        dp[next][end + next] = check(next, end + next)


print(dp[0][N - 1])