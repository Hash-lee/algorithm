import sys
sys.stdin = open('sample.txt', 'r')


# 크루스칼




'''
def bridge(n):
    v[n] = 1
    mn = 1000000**2*2+1
    idx = -1
    for i in range(N):
        if v[i] == 0:
            if arr[n][i] < c[i]:
                c[i] = arr[n][i]
            if c[i] < mn:
                mn = arr[n][i]
                idx = i
    return idx

for tc in range(1, int(input())+1):
    N = int(input())
    island = [0] * N
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    for i in range(N):
        island[i] = a[i],b[i]

    E = float(input())
    arr = [[0]* (N) for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            arr[i][j] = arr[j][i] = round(((island[i][0] - island[j][0])**2 + (island[i][1] - island[j][1])**2) * E)
'''