import sys

T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    cost = int(sys.stdin.readline())

    coins.sort(reverse=True)
    check = [0] * (cost + 1)
    check[0] = 1

    for coin in coins:
        for idx in range(1, cost + 1):
            if coin <= idx:
                check[idx] += check[idx - coin]

    print(check[cost])