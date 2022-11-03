import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.append([])
def partial(array, idx, n, s):
    if n:
        for i in range(idx, len(array) - n):
            partial(array, i + 1, n - 1, s + array[i])
    else:
        array[-1].append(s)


for i in range(1, len(arr)):
    partial(arr, 0, i, 0)

counts = 0
for one in arr[-1]:
        if S == one:
            counts += 1
print(counts)