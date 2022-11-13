import sys


N, M = map(int, sys.stdin.readline().split())

arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    heavy, light = map(int, sys.stdin.readline().split())
    arr[heavy][light] = 1

heavier = [0] * (N + 1)
lighter = [0] * (N + 1)


for idx in range(1, N + 1):
    visit = [1] * (N + 1)
    visit[idx] = 0
    Q = [0] * 100
    front = -1
    rear = -1
    for col in range(1, N + 1):
        if arr[idx][col] and visit[col]:
            rear += 1
            visit[col] = 0
            Q[rear] = col
            lighter[idx] += 1
    while front < rear:
        front += 1
        row = Q[front]
        for col in range(1, N + 1):
            if arr[row][col] and visit[col]:
                rear += 1
                visit[col] = 0
                Q[rear] = col
                lighter[idx] += 1

for idx in range(1, N + 1):
    visit = [1] * (N + 1)
    visit[idx] = 0
    Q = [0] * 100
    front = -1
    rear = -1
    for row in range(1, N + 1):
        if arr[row][idx] and visit[row]:
            rear += 1
            visit[row] = 0
            Q[rear] = row
            heavier[idx] += 1
    while front < rear:
        front += 1
        col = Q[front]
        for row in range(1, N + 1):
            if arr[row][col] and visit[row]:
                rear += 1
                visit[row] = 0
                Q[rear] = row
                heavier[idx] += 1

counts = 0
for idx in range(1, N + 1):
    if N // 2 < heavier[idx] or N // 2 < lighter[idx]:
        counts += 1

print(counts)