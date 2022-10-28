import sys

N = sys.stdin.readline().rstrip()
n = int(N)


count = 0
if n < 100:
    count = n
else:
    count = 99
    for i in range(111, n + 1):
        lst = list(map(int, (" ".join(str(i))).split()))
        if lst[0] - lst[1] == lst[1] - lst[2]:
            count += 1
print(count)