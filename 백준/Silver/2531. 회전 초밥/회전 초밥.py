import sys

N, d, k, c = map(int, input().split())
sushi = list(map(int, sys.stdin.readlines()))
include = [0] * (d + 1)
include[c] = 100000
var = 1
for idx in range(k):
    if not include[sushi[idx]]:
        var += 1
    include[sushi[idx]] += 1
mx = var
for s in range(N):
    e = (s + k) % N
    if not include[sushi[e]]:
        var += 1
    include[sushi[e]] += 1
    include[sushi[s]] -= 1
    if not include[sushi[s]]:
        var -= 1
    mx = max(mx, var)
print(mx)