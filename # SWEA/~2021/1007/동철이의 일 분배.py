import sys
sys.stdin=open('sample.txt', 'r')

def per(n, p):
    global prob
    if n == 0 and p > prob:
            prob = p
    for i in range(N):
        if visited[i] == 0 and p*arr[N-n][i]/100 > prob:
            p = p*arr[N-n][i]/100
            visited[i] = 1
            per(n-1, p)
            visited[i] = 0
            p = p/arr[N-n][i]*100

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    prob = 0
    visited = [0] * N

    per(N, 1)
    print('#{0} {1:0.6f}'.format(tc, prob* 100))