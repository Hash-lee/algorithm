import sys
sys.setrecursionlimit(10**5)

N = int(sys.stdin.readline())
group = {i : i for i in range(N)}
lines = [[0] * 4 for _ in range(N)]
values = [0] * N
mx = -1
count = 0


def find(x):
    if group[x] == x:
        return x
    else:
        group[x] = find(group[x])
        return find(group[x])


def union(n1, n2):
    group[find(n2)] = n1


def CCW(i, j):
    x1, y1, x2, y2 = lines[i]
    x3, y3, x4, y4 = lines[j]
    d1 = (x1*y3 + x3*y4 + x4*y1) - (x3*y1 + x4*y3 + x1*y4)
    d2 = (x2*y3 + x3*y4 + x4*y2) - (x3*y2 + x4*y3 + x2*y4)
    return d1, d2


def check(i, j):
    x1, y1, x2, y2 = lines[i]
    x3, y3, x4, y4 = lines[j]
    if x4 < x1 or x2 < x3: return False
    if max(y3, y4) < min(y1, y2) or max(y1, y2) < min(y3, y4): return False
    if (x1, y1) == (x3, y3) or (x1, y1) == (x4, y4) or (x2, y2) == (x3, y3) or (x2, y2) == (x4, y4): return True
    d1, d2 = CCW(i, j)
    d3, d4 = CCW(j, i)
    if d1 * d2 == 0:
        return True if d1 == d2 or d3 * d4 < 0 else False
    return True if d1 * d2 < 0 and d3 * d4 <= 0 else False

for i in range(N):
    x1, y1, x2, y2 = map(float, sys.stdin.readline().split())
    if x1 > x2: x1, y1, x2, y2 = x2, y2, x1, y1
    
    lines[i] = [x1, y1, x2, y2]
    for j in range(i):
        if find(group[j]) != i and check(i, j): union(i, j)


for i in range(N):
    x = find(i)
    values[x] += 1
    if values[x] == 1: count += 1
    mx = max(mx, values[x])

print(count)
print(mx)