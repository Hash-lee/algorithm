import sys

shorts = list(map(int, sys.stdin.readlines()))
duo = sum(shorts) - 100
for i in range(8):
    for j in range(i + 1, 9):
        if shorts[i] + shorts[j] == duo:
            shorts[i] = 0xFFF
            shorts[j] = 0xFFF
            duo = False
            break
    if not duo:
        break
shorts.sort()
for s in shorts[:7]:
    print(s)