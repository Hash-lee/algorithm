import sys

K, L = map(int, sys.stdin.readline().split())
dct = {sys.stdin.readline().strip(): i for i in range(L)}
print("\n".join(sorted(dct.keys(), key=lambda x: dct[x])[:K]))
