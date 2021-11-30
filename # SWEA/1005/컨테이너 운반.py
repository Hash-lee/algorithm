import sys; sys.stdin = open('sample.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort()

    bw = sum(w)
    for j in range(len(w)):
        for i in range(len(t)):
            if w[j] <= t[i]:
                t[i] = -1
                w[j] = 0
                break
    aw = sum(w)

    print('#{} {}'.format(tc, bw-aw))
