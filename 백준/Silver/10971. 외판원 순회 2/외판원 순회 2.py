import sys

N = int(sys.stdin.readline())
arr = [list(map(int, n.split())) for n in sys.stdin.readlines()]

V = [1] * N

mn = 0xFFFFFFFF


def btf(start, r, s=0, n=0):
    global mn
    if s > mn:
        return
    if n == N and r == start:
        if s < mn:
            mn = s
        return

    for c in range(N):
        if c != r and V[c] and arr[r][c]:
            V[c] = 0
            btf(start, c, s + arr[r][c], n + 1)
            V[c] = 1


for i in range(N):
    btf(i, i)


print(mn)