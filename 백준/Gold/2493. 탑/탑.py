import sys

N = int(sys.stdin.readline())
towers = [1000000001] + list(map(int, sys.stdin.readline().split()))
deliver = [0] + [n for n in range(N)]


def through(idx, height):
    return deliver[idx] if height < towers[deliver[idx]] else through(deliver[idx], height)


for idx in range(1, N + 1):
    deliver[idx] = through(idx, towers[idx])

print(" ".join(list(map(str, deliver[1:]))))