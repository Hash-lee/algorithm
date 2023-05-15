N = int(input())

if N < 3:
    a = 0
    for _ in range(N):
        a += int(input())
    print(a)
else:
    stairs = [0] * (N)
    for i in range(N):
        stairs[i] = int(input())

    V = [[0, 0] for _ in range(N)]
    V[0] = [stairs[0], stairs[0]]
    V[1] = [stairs[1], stairs[0]+stairs[1]]

    for i in range(2, N):
        V[i][0] = max(V[i-2]) + stairs[i]
        V[i][1] = V[i-1][0] + stairs[i]

    print(max(V[-1]))