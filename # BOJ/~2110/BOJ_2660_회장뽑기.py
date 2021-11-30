import sys; sys.stdin = open('sample.txt', 'r')

N = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]

flag = 1
while flag:
    line = list(map(int, input().split()))
    if line[0] > 0:
        arr[line[0]][line[1]] = arr[line[1]][line[0]] = 1
    else: flag = 0

# BFS, 가까운 경로가 뒤에 나올 경우 포함
def FIND(n, m, k):
    if arr[n][m] == 1 and (visited[m] == 0 or visited[m] > k):
        visited[m] = k
    else:
        for i in range(1, N+1):
            if arr[n][i] == 1 and (visited[i] == 0 or visited[i] > k):
                visited[i] = k
                FIND(i, m, k+1)

for n in range(1, N):
    for m in range(n+1, N+1):
        if arr[n][m] == 0:
            visited = [0] * (N+1)
            FIND(n, m, 1)
            arr[n][m] = arr[m][n] = visited[m]

points = []
for a in arr:
    points.append(max(a))

point = 9999
who = []
cnt = 1
for i in range(1, N+1):
    if points[i] < point:
        point = points[i] 
        who = [i]
        cnt = 1
    elif points[i] == point:
        cnt += 1
        who.append(i)

print(point, cnt)
print(" ".join(list(map(str, who))))