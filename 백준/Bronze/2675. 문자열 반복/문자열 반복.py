import sys

T = int(sys.stdin.readline())
for tc in range(T):
    R, S = sys.stdin.readline().split()
    for s in S:
        print(s * int(R), end="")
    print("")
