N = int(input())

Q0 = []
Q1 = []
cnt = 0
for r in range(N):
    sen = input().split()
    for c in range(N):
        if sen[c] == '1':
            if (r+c)%2: Q0.append((r, c))
            else:Q1.append((r, c))

ans0, ans1 = -1, -1
l0, l1 = len(Q0), len(Q1)
VR0, VL0, VR1, VL1 = [1]*(N*2-1), [1]*(N*2-1), [1]*(N*2-1), [1]*(N*2-1)

def bishop(s, k, n=0):
    if k == 0:
        global ans0
        if s < ans0: return
        if n == l0:
            if ans0 < s:
                ans0 = s
        else:
            a, b = Q0[n]
            r = a+b
            c = a+N-1-b
            if VR0[r] and VL0[c]:
                VR0[r], VL0[c] = 0, 0
                bishop(s, k, n+1)
                VR0[r], VL0[c] = 1, 1
            bishop(s-1, k, n+1)

    elif k == 1:
        global ans1
        if s < ans1: return
        if n == l1:
            if ans1 < s:
                ans1 = s
        else:
            a, b = Q1[n]
            r = a+b
            c = a+N-1-b
            if VR1[r] and VL1[c]:
                VR1[r], VL1[c] = 0, 0
                bishop(s, k, n+1)
                VR1[r], VL1[c] = 1, 1
            bishop(s-1, k, n+1)

bishop(l0, 0)
bishop(l1, 1)
print(ans0 + ans1)