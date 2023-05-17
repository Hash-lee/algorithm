import sys
from collections import deque
N = int(sys.stdin.readline())
visited = [False] * (N+1)

Q = deque([N])
visited[N] = (0, N)
while Q:
    n = Q.popleft()
    c = visited[n][0]
    if n == 1: break
    if not n % 3:
        if visited[n // 3] == False or c+1 < visited[n // 3][0]:
            visited[n // 3] = (c+1, n)
            Q.append(n // 3)
    if not n % 2:
        if visited[n // 2] == False or c+1 < visited[n // 2][0]:
            visited[n // 2] = (c+1, n)
            Q.append(n // 2)
    if visited[n - 1] == False or c+1 < visited[n - 1][0]:
        visited[n - 1] = (c+1, n)
        Q.append(n - 1)

log = [1]
while log[-1] != visited[log[-1]][1]:
    log.append(visited[log[-1]][1])

print(visited[1][0])
print(*log[::-1])