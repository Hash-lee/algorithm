import sys

N, K = map(int, sys.stdin.readline().split())


usages = list(map(int, sys.stdin.readline().split()))
order = {i: [] for i in range(1, K + 1)}

occupied = []
cnt = -1
while len(occupied) < N and cnt < K:
    cnt += 1
    if usages[cnt] in occupied:
        continue
    else:
        occupied.append(usages[cnt])

for i in range(cnt + 1, K):
    order[usages[i]].append(i + 1)
plug = 0
for i in range(1, K + 1):
    order[i].sort(reverse=True)

for i in range(cnt + 1, K):
    order[usages[i]].pop()
    if usages[i] in occupied:
        continue
    target = -1
    mx = -1
    for idx in range(N):
        num = occupied[idx]
        if not order[num]:
            target = idx
            break
        else:
            if mx < order[num][-1]:
                mx = order[num][-1]
                target = idx
    plug += 1
    if target != -1:
        occupied[target] = usages[i]


print(plug)