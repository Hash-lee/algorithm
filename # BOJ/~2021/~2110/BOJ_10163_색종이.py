#53점
T = int(input())
P = [[0] * 1001 for _ in range(1001)]


for t in range(T):
    x, y, w, h = map(int, input().split())
    for r in range(x, x + w):
        for c in range(y, y + h):
            P[r][c] = t+1

n = [0] * T

for py in P:
    for px in range(1001):
        if py[px] != 0:
            n[py[px]-1] += 1

for a in n:
    print(a)