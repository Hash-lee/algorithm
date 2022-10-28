import sys

lst = [sys.stdin.readline() for _ in range(2)]
n = int(lst[0])
m = int(lst[1])
x = str(m)

answer_lst = [n * int(x[s]) for s in range(-1, -4, -1)]
for l in answer_lst:
    print(l)
print(n * m)