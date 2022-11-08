import sys

N = int(sys.stdin.readline())

Q = [0] * N
front = -1
rear = -1

for _ in range(N):
    ipt = sys.stdin.readline().strip()
    if ipt[:3] == "pus":
        ipt, n = ipt.split()
        rear += 1
        Q[rear] = n
    elif ipt[:3] == "pop":
        if front < rear:
            front += 1
            print(Q[front])
        else:
            print(-1)
    elif ipt[:3] == "siz":
        print(rear - front)
    elif ipt[:3] == "emp":
        print(0) if front < rear else print(1)
    elif ipt[:3] == "fro":
        print(Q[front + 1]) if front < rear else print(-1)
    elif ipt[:3] == "bac":
        print(Q[rear]) if front < rear else print(-1)