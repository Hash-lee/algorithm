T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))
    print('#{} {}'.format(t, Q[M%N]))