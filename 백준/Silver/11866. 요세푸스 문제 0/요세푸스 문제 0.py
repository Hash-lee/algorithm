import sys

N, K = map(int, sys.stdin.readline().split())
Q = [n + 1 for n in range(N)]
front = -1


kill = N
yose = []
while kill:
    k = 0
    while k < K:
        front = (front + 1) % N
        if Q[front]:
            k += 1
    yose.append(Q[front])
    Q[front] = 0
    kill -= 1

print("<" + ", ".join(list(map(str, yose))) + ">")