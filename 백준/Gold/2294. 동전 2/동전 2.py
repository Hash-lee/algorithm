import sys

N, K = map(int, sys.stdin.readline().split())
moneys = set()
for s in sys.stdin.readlines():
    n = int(s)
    if n < K:
        moneys.add(n)
    elif n == K:
        print(1)
        exit()

moneys = sorted(list(moneys), reverse=True)

coins = 0xFFFFF

Q = [0] * 100000
front = -1
rear = 0
Q[rear] = (K, 0)


flag = False
visit = [1] * (K + 1)
visit[K] = 0
while front < rear:
    front += 1
    balance, counts = Q[front]
    if balance:
        for money in moneys:
            if money <= balance and visit[balance - money]:
                visit[balance - money] = 0
                rear += 1
                Q[rear] = (balance - money, counts + 1)
    else:
        flag = True
        coins = counts
        break
if flag:
    print(coins)
else:
    print(-1)