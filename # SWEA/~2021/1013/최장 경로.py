import sys
sys.stdin = open('sample.txt', 'r')


def distance(a, b):
    for i in range(1, N+1):
        if arr[a][i] == 1 and visited[i] == 0:
            if i != b:
                visited[i] = 1
                lenth[i] = lenth[a] + 1
                distance(i, b)
                visited[i] = 0
            elif i == b:
                if lenth[b] < lenth[a]+1:
                    lenth[b] = lenth[a]+1

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    for m in range(M):
        s, e = map(int, input().split())
        arr[s][e] = arr[e][s] = 1

    answer = 1
    for a in range(1, N):
        for b in range(a+1, N+1):
            visited = [0] * (N+1)
            lenth = [1] * (N+1)

            visited[a] = 1
            distance(a, b)
            d = lenth[b]
            if d > answer: answer = d
            
    
    print('#{} {}'.format(tc, answer))