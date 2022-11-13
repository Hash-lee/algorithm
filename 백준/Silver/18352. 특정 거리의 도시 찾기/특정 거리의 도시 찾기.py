import sys

N, M, K, X = map(int, sys.stdin.readline().split())
path = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    path[s].append(e)

Q = [0] * N
front = -1
rear = 0
Q[rear] = (X, 0)
visit = [1] * (N + 1)
visit[X] = 0

right = []
flag = True
while front < rear:
    front += 1
    city, cost = Q[front]
    if cost == K:
        flag = False
        right.append(city)
    elif cost < K:
        for des in path[city]:
            if visit[des]:
                rear += 1
                Q[rear] = (des, cost + 1)
                visit[des] = 0


if flag:
    print(-1)
else:
    for city in sorted(right):
        print(city)