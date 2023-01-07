import sys

K, L = map(int, sys.stdin.readline().split())
check = set()
aligned = []

applier = list(map(lambda x: x.strip(), sys.stdin.readlines()))
for idx in range(-1, -L - 1, -1):
    if not applier[idx] in check:
        check.add(applier[idx])
        aligned.append(applier[idx])

K = len(aligned) if len(aligned) < K else K
for idx in range(-1, -K - 1, -1):
    print(aligned[idx])