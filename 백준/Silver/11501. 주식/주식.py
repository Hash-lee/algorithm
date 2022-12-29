import sys

T = int(sys.stdin.readline())
for tc in range(1, T + 1):
    N = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))[::-1]
    income = 0
    mx = prices[0]
    for idx in range(1, N):
        price = prices[idx]
        if price < mx: income += mx-price
        else: mx = price
    print(income)