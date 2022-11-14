import sys

N, M = map(int, sys.stdin.readline().split())

points = [0 for _ in range(N + 1)]
linked = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    tall, short = map(int, sys.stdin.readline().split())
    linked[tall].append(short)
    points[short] += 1

Q = [0] * N
front = -1
rear = -1

srted = []

for idx in range(1, N + 1):
    if points[idx] == 0:
        rear += 1
        Q[rear] = idx
        srted.append(str(idx))

while front < rear:
    front += 1
    now = Q[front]
    for next in linked[now]:
        points[next] -= 1
        if points[next] == 0:
            rear += 1
            Q[rear] = next
            srted.append(str(next))


print(" ".join(srted))