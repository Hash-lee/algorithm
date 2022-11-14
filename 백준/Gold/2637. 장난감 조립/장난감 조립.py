import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

parts = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().split())
    parts[X].append((Y, K))

needs = [0] * (N + 1)
needs[N] = 1


Q = [0] * (N**2)
front = -1
rear = 0
Q[rear] = N


def BFS_cycle(Q, front, rear):
    tmp_Q = [0] * N
    tmp_front = -1
    tmp_rear = -1
    while front < rear:
        front += 1
        part_now = Q[front]
        need_now = needs[part_now]
        needs[part_now] = 0

        for sub_part in parts[part_now]:
            sub_part_num, need_sub_part = sub_part
            needs[sub_part_num] += need_sub_part * need_now

    for idx in range(1, N + 1):
        if needs[idx] and parts[idx]:
            tmp_rear += 1
            tmp_Q[tmp_rear] = idx
    return tmp_Q, tmp_front, tmp_rear


while front < rear:
    Q, front, rear = BFS_cycle(Q, front, rear)


for idx in range(1, N + 1):
    if not parts[idx]:
        print(idx, needs[idx])