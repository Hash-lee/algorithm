N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

V = [[[0] * 3 for _ in range(N)] for _ in range(N)]
V[0][1][0] = 1

def vrf(r, c):
    if r < N and c < N and arr[r][c] == 0:
        return True
    return False

def pipe(r, c):
    if V[r][c][0]:
        if vrf(r, c+1):
            V[r][c+1][0] += V[r][c][0]
            if vrf(r+1, c) and vrf(r+1, c+1):
                V[r+1][c+1][2] += V[r][c][0]
    if V[r][c][1]:
        if vrf(r+1, c):
            V[r+1][c][1] += V[r][c][1]
            if vrf(r, c+1) and vrf(r+1, c+1):
                V[r+1][c+1][2] += V[r][c][1]
    if V[r][c][2]:
        if vrf(r, c+1):
            V[r][c+1][0] += V[r][c][2]
        if vrf(r+1, c):
            V[r+1][c][1] += V[r][c][2]
        if vrf(r+1, c) and vrf(r, c+1) and vrf(r+1, c+1):
            V[r+1][c+1][2] += V[r][c][2]

for k in range(1, 2*N-1):
    for r in range(k+1):
        if r < N and k-r < N:
            pipe(r, k-r)

print(sum(V[N-1][N-1]))