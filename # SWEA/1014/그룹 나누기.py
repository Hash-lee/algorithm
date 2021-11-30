import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    V = [[i] for i in range(N+1)]
    for i in range(0, M * 2 - 1, 2):
        r, s = arr[i], arr[i+1]
        V[r] += V[s]
        for k in V[r]:
            V[k] = V[r]
    answer = []
    cnt = 0
    for v in V[1:]:
        if not v in answer:
            answer.append(v)
            cnt += 1
    print('#{} {}'.format(tc, cnt))
    