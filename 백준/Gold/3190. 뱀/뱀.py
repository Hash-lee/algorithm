import sys

N = int(sys.stdin.readline())
arr = [[0] * N for _ in range(N)]

K = int(sys.stdin.readline())
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    arr[r - 1][c - 1] = 1

L = int(sys.stdin.readline())
changes = []
for _ in range(L):
    X, D = sys.stdin.readline().split()
    changes.append([int(X), D])

dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]
snake_Q = [0] * (N**2)
snake_Q[0] = (0, 0)
head = 0
tail = 0

direct = 0
seconds = 0
changes_idx = 0
while True:
    seconds += 1
    head_r, head_c = snake_Q[head]
    tail_r, tail_c = snake_Q[tail]
    new_loc_r = head_r + dir_r[direct]
    new_loc_c = head_c + dir_c[direct]
    if 0 <= new_loc_r < N and 0 <= new_loc_c < N:
        head += 1
        snake_Q[head] = (new_loc_r, new_loc_c)
        if arr[new_loc_r][new_loc_c] == 2:
            break
        else:
            if not arr[new_loc_r][new_loc_c]:
                arr[tail_r][tail_c] = 0
                tail += 1
            arr[new_loc_r][new_loc_c] = 2
    else:
        break
    if changes_idx < L and changes[changes_idx][0] == seconds:
        if changes[changes_idx][1] == "L":
            direct = (direct + 3) % 4
        elif changes[changes_idx][1] == "D":
            direct = (direct + 1) % 4
        changes_idx += 1

print(seconds)
