import sys

N = sys.stdin.readline()
n = int(N)

for i in range(1, 10):
    r = n * i
    print(n,"*",i,"=",r)