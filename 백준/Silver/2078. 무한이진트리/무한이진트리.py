import sys
from collections import deque

L, R = map(int, sys.stdin.readline().split())
root = (L, R, 0, 0)
Q = deque()

Q.append(root)

while Q:
    l, r, left, right = Q.popleft()
    if l == 1 or r == 1:
        print(left + ((l - 1) // r), right + ((r - 1) // l))
        break

    if l > r:
        Q.append((l - (r * (l // r)), r, left + (l // r), right))
    elif r > l:
        Q.append((l, r - (l * (r // l)), left, right + (r // l)))
