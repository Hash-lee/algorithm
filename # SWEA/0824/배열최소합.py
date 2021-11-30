T = int(input())


def P(k, N):
    global result
    if k == N:
        if sum(order) < result:
            result = sum(order)
    else:
        for i in range(N):
            if visited[i]: continue
            order[k] = arr[k][i]
            visited[i] = 1
            if sum(order[:k]) < result:
                P(k + 1, N)
            visited[i] = 0

for t in range(1, T+1):
    N = int(input())

    arr = [0] * N
    for n in range(N):
        arr[n] = list(map(int, input().split()))


    visited = [0] * N
    order = [0] * N
    result = 5000



    P(0,N)

    print('#{} {}'.format(t, result))