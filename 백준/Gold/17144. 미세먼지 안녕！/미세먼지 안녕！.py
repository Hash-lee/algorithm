R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def diffusion(r, c):
    m = dust[100*r + c] // 5
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
            arr[r][c] -= m
            arr[nr][nc] += m

dust = {}
airflow = []
for r in range(R):
    if arr[r][0] == -1:
        airflow.append((r, 0))
    for c in range(C):
        if arr[r][c] > 0:
            dust[100*r + c] = arr[r][c]

def flow():
    for a in range(2):
        r = airflow[a][0]
        c = airflow[a][1]
        idx = 0
        
        if a == 0:
            d1 = [-1, 0, 1, 0]
            d2 = [0, 1, 0, -1]
            while True:
                nr = r + d1[idx]
                nc = c + d2[idx]
                if 0 <= nr <= airflow[a][0] and 0 <= nc < C:
                    if arr[r][c] != -1:
                        arr[r][c] = arr[nr][nc]
                    if arr[nr][nc] == -1:
                        arr[r][c] = 0
                        break
                    r, c = nr, nc
                else: idx += 1
        
        elif a == 1:
            d1 = [1, 0, -1, 0]
            d2 = [0, 1, 0, -1]
            while True:
                nr = r + d1[idx]
                nc = c + d2[idx]
                if airflow[a][0] <= nr < R and 0 <= nc < C:
                    if arr[r][c] != -1:
                        arr[r][c] = arr[nr][nc]
                    if arr[nr][nc] == -1:
                        arr[r][c] = 0
                        break
                    r, c = nr, nc
                else: idx += 1


for _ in range(T):
    dif = tuple(dust.keys())
    for d in dif:
        r = d // 100
        c = d % 100
        diffusion(r, c)
    
    flow()

    dust = {}
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:
                dust[100*r + c] = arr[r][c]


print(sum(dust.values()))