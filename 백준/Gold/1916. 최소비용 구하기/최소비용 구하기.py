import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = [[-1 for _ in range(N + 1)] for __ in range(N + 1)]
costs = [100000001 for _ in range(N + 1)]
for _ in range(M):
    s, e, cost = map(int, sys.stdin.readline().split())
    if arr[s][e] == -1:
        arr[s][e] = cost
    else:
        if cost < arr[s][e]:
            arr[s][e] = cost

start, finish = map(int, sys.stdin.readline().split())
costs[start] = 0

Q = [0] * (N**2)
front = -1
rear = 0
Q[0] = (start, 0)

mn = 100000001
while front < rear:
    front += 1
    city, pay = Q[front]
    if city == finish:
        if costs[city] < mn:
            mn = costs[city]
    for idx in range(1, N + 1):
        if 0 <= arr[city][idx]:
            if pay + arr[city][idx] < costs[idx]:
                rear += 1
                Q[rear] = (idx, pay + arr[city][idx])
                costs[idx] = pay + arr[city][idx]

print(mn)