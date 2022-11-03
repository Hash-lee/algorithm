import sys

def recurs(n):
    if n:
        for i in range(1, min(n + 1, 4)):
            recurs(n - i)
    else:
        global count
        count += 1


TC = int(sys.stdin.readline())
for tc in range(TC):
    N = int(sys.stdin.readline())
    count = 0
    recurs(N)
    print(count)
