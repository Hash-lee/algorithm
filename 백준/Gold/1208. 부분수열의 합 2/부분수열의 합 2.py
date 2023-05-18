import sys
N, S = map(int, sys.stdin.readline().split())
numbers = sorted(map(int, sys.stdin.readline().split()))
ans = 0

res1 = [0]
for idx in range(N//2):
    for j in range(len(res1)):
        res1.append(res1[j] + numbers[idx])

res2 = [0]
for idx in range(N//2, N):
    for j in range(len(res2)):
        res2.append(res2[j] + numbers[idx])
res1.sort()

find = {}
for r2 in res2:
    find[r2] = find[r2] + 1 if r2 in find else 1

for r1 in res1:
    if (S - r1) in find: ans += find[S - r1]

print(ans if S else ans-1)