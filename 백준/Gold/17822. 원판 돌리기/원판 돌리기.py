import sys
sys.setrecursionlimit(10**5)

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
rules = [tuple(map(int, input().split())) for _ in range(T)]


def turn(x, d, k):
    if d == 0: k = M-k
    for i in range(0+x-1, N, x):
        tmp_lst = [0] * M
        for j in range(M):
            tmp_lst[j] = arr[i][(j+k) % M]
        arr[i] = tmp_lst[:]

        
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def BFS(r, c, x):
    for k in range(4):
        nr = r + dr[k]
        nc = (c + dc[k] + M) % M
        if 0 <= nr < N and arr[nr][nc] == x:
            arr[r][c] = 0
            arr[nr][nc] = 0
            global flag
            flag = 0
            BFS(nr, nc, x)

for i in range(T):
    x, d, k = rules[i]
    turn(x, d, k)
    flag = 1
    s = 0
    cnt = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c]:
                s += arr[r][c]
                cnt += 1
                BFS(r, c, arr[r][c])
    if cnt == 0: break
    if flag:
        avg = s / cnt
        for r in range(N):
            for c in range(M):
                if arr[r][c]:
                    if arr[r][c] < avg: arr[r][c] += 1
                    elif arr[r][c] > avg: arr[r][c] -= 1

answer = 0
for a in arr:
    answer += sum(a)
print(answer)