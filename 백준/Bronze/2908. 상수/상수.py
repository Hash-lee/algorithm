import sys

print(max(map(lambda x: int(x[::-1]), sys.stdin.readline().split())))