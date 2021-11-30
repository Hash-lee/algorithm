import sys
sys.stdin = open('fast.txt', 'r')


T = int(input())

for t in range(T):
    A, B = input().split()

    la = len(A)
    lb = len(B)

    typ = 0
    n = 0

    while n <= la -lb:
        if lb == 1:
            typ = la
            break

        if A[n] != B[0]:
            typ += 1
            n += 1
        elif A[n] == B[0]:
            tmp = 1
            for m in range(1, lb):
                if A[n+m] == B[m]:
                    tmp += 1
            if tmp == lb:
                typ += 1
                n += lb
            else:
                typ += 1
                n += 1
        if la - lb < n:
            typ += (la - n)

    print('#{} {}'.format(t+1, typ))