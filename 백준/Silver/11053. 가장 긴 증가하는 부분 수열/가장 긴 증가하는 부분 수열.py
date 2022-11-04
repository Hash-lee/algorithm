import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
path = [1] * N
for now_idx in range(1, N):
    for past_idx in range(now_idx):
        if arr[past_idx] < arr[now_idx]:
            if path[now_idx] < path[past_idx] + 1:
                path[now_idx] = path[past_idx] + 1

print(max(path))