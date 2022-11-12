import sys

N = int(sys.stdin.readline())


tree = {}
for _ in range(N - 1):
    left, right = map(int, sys.stdin.readline().split())
    try:
        tree[left].append(right)
    except:
        tree[left] = [right]
    try:
        tree[right].append(left)
    except:
        tree[right] = [left]

mother = [0] * (N + 1)
visit = [1] * (N + 1)
visit[1] = 0

Q = [0] * N
front = -1
rear = 0
Q[rear] = 1


while front != rear:
    front += 1
    mom = Q[front]
    if tree.get(mom, 0):
        for d in tree[mom]:
            if visit[d]:
                visit[d] = 0
                mother[d] = mom
                rear += 1
                Q[rear] = d

for mom in mother[2:]:
    print(mom)