import sys

N = int(sys.stdin.readline())
Q = [n + 1 for n in range(N)]
front = 0
rear = -1
while Q[front] != Q[rear]:
    front = (front + 1) % N
    rear = (rear + 1) % N
    Q[rear] = Q[front]
    front = (front + 1) % N

print(Q[front])