import sys

N,d,k,c=map(int, input().split())
l=list(map(int, sys.stdin.readlines()))
l+=l[:k]
print(max([len(set(l[i:i+k])|set([c])) for i in range(N)]))