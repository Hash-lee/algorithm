import sys
from math import ceil

A, B, V = map(int, sys.stdin.readline().split())
print(ceil((V - A) / (A - B)) + 1)