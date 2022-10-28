import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()


l = len(A)
V = [1 for _ in range(l)]

answer = 0


def btf(s, p, n):
    if n == l:
        global answer
        if answer < s:
            answer = s
        return
    for i in range(l):
        if V[i]:
            V[i] = 0
            if n == 0:
                btf(s, A[i], n + 1)
            else:
                btf(s + abs(p - A[i]), A[i], n + 1)
            V[i] = 1


btf(0, 0, 0)
print(answer)