import sys


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * (2**N) for _ in range(N)]


def dynamic(prev, code):
    if code:
        mn = 0xFFFFFFFFFF
        for next in range(1, N):
            if arr[prev][next] and code & (1 << next):
                code &= ~(1 << next)
                p = dp[next][code] if dp[next][code] else dynamic(next, code)
                x = arr[prev][next] + p
                if x < mn:
                    mn = x
                code |= 1 << next
        dp[prev][code] = mn
        return mn
    else:
        return arr[prev][0] if arr[prev][0] else 0xFFFFFFFFFF


code = 0
code = 1 << N
code -= 2

mn = dynamic(0, code)
print(mn)