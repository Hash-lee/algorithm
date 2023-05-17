import sys
T = int(sys.stdin.readline())
for tc in range(T):
    N, K = map(int, sys.stdin.readline().split())
    spends = list(map(int, sys.stdin.readline().split()))
    keys = {i:[] for i in range(N)}
    locks = [0] * N
    start = [0] * N

    for _ in range(K):
        F, B = map(lambda x: int(x)-1, sys.stdin.readline().split())
        keys[F].append(B)
        locks[B] += 1

    W = int(sys.stdin.readline()) - 1
    available = []
    for i in range(N):
        if locks[i] == 0:
            available.append(i)
    
    while True:
        target = available.pop()
        if target == W:
            print(start[W] + spends[W])
            break
        else:
            for key in keys[target]:
                locks[key] -= 1
                start[key] = max(start[key], start[target]+spends[target])
                if locks[key] == 0:
                    available.append(key)