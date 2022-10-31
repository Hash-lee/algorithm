import sys

N = int(sys.stdin.readline())

k = 2
while N > 1:
    if not N % k:
        print(k)
        N = N // k
    else:
        k += 1