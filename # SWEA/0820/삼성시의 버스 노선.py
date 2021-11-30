import sys
sys.stdin = open('s1.txt', 'r')


T = int(input())

for t in range(1, T+1):
    station = [0] * 5001

    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            station[i] += 1

    P = int(input())
    thru = [0] * (P)

    for p in range(P):
        j = int(input())
        thru[p] = str(station[j])

    print('#{} {}'.format(t, " ".join(thru)))