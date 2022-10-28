import sys

sys.stdin.readline()
lst = "\n".join(map(str, sorted(map(int, sys.stdin.readlines()))))
print(lst)