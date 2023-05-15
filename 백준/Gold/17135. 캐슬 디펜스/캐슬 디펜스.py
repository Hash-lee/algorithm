N, M, D = map(int, input().split())
arr = [0] * N

for n in range(N-1, -1, -1):
    arr[n] = tuple(map(int, input().split()))

archer = []
V = []

def sc(n=0, s=0):
    if n == M:
        if s == 3:
            archer.append(V[:])
    else:
        sc(n+1, s)
        V.append(n)
        sc(n+1, s+1)
        V.pop()
sc()

def shoot(i, n=0):
    if n == N: return 0
    target = arr[n:n+D]
    kill = 0

    for A in archer[i]:
        distance = 1000
        x = 0

        r = 0
        for t in target:
            for m in range(M):
                if t[m]:
                    d = r + 1 + abs(A-m)
                    if d < distance and n <= V[n+r][m]:
                        distance = d
                        x = (n+r, m)
                    elif d == distance and m < x[1] and n <= V[n+r][m]:
                        x = (n+r, m)
            r += 1
        
        if x != 0 and distance <= D:
            if V[x[0]][x[1]] == 100:
                kill += 1
            V[x[0]][x[1]] = n
    return kill + shoot(i, n+1)

result = 0
for i in range(len(archer)):
    V = [[100] * M for _ in range(N)]
    tmp = shoot(i)
    if result < tmp:
        result = tmp
print(result)