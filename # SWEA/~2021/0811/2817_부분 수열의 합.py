# 안 보고 풀어보기
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    cnt = 0
    for j in range(1<<N):
        ps = 0
        for k in range(N+1):
            if j & (1<<k):
                ps += numbers[k]
        if ps == K:
            cnt += 1
    print('#{} {}'.format(i+1, cnt))