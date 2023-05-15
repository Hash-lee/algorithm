N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

house = []
chiken = []

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1: house.append((r, c))
        if arr[r][c] == 2: chiken.append((r, c))

H = len(house)
C = len(chiken)

dist = [[0]*C for _ in  range(H)]

for r in range(H):
    for c in range(C):
        dist[r][c] = abs(house[r][0] - chiken[c][0]) + abs(house[r][1] - chiken[c][1])


open = [1] * C
result = 0xffffffffffffff
ttt = []
def close(n=0, c=0):
    if n == C:
        if c == (C-M):
            tmp_sum = 0
            for r in range(H):
                tmp = 0xffff
                for c in range(C):
                    if open[c] == 1 and dist[r][c] < tmp:
                        tmp = dist[r][c]
                tmp_sum += tmp
            global result
            if tmp_sum < result:
                result = tmp_sum
    else:
        close(n+1, c)
        open[n] = 0
        close(n+1, c+1)
        open[n] = 1

close()
print(result)