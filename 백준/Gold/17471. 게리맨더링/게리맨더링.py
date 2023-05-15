N = int(input())
pop = [0] + list(map(int, input().split()))
arr = [[0]*(N+1) for _ in range(N+1)]

for r in range(1,N+1):
    l = list(map(int, input().split()))
    for c in l[1:]:
        arr[r][c], arr[c][r] = 1, 1

result = -1

def bfs(s, e, lst):
    visited[s] = 1
    for i in range(1, N+1):
        if arr[s][i] == 1 and visited[i] == 0 and i in lst:
            if i == e:
                global flag
                flag = 1
            else: bfs(i, e, lst)

def vf(lst):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            global visited, flag
            visited = [0] * (N+1)
            flag = 0
            bfs(lst[i], lst[j], lst)
            if flag == 0: return 0
    return 1


             

L = []
R = []
def sc(n=2):
    if n == N+1:
        l = [1, ]
        r = []
        for i in range(2, N+1):
            if V[i] == 1: r.append(i)
            else: l.append(i)
        if r == []: return
        L.append(l)
        R.append(r)
    else:
        sc(n+1)
        V[n] = 1
        sc(n+1)
        V[n] = 0

if N == 2:
    print(abs(pop[1]-pop[2]))
else:
    V = [0] * (N+1)
    V[1] = 1
    sc()

    for i in range(len(L)):
        if vf(L[i]) and vf(R[i]):
            sum_l, sum_r = 0, 0
            for l in L[i]:
                sum_l += pop[l]
            for r in R[i]:
                sum_r += pop[r]
            s = abs(sum_l-sum_r)
            if result == -1 or result > s:
                result = s
    print(result)