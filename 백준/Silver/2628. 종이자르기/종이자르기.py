import sys

width, height = map(int, sys.stdin.readline().split())
cut = int(sys.stdin.readline())

vertical = [0, width]
horizontal = [0, height]
for _ in range(cut):
    dir, point = map(int, sys.stdin.readline().split())
    if dir:
        vertical.append(point)
    else:
        horizontal.append(point)

vertical.sort()
horizontal.sort()


def result(lst):
    for i in range(-1, -len(lst), -1):
        lst[i] = lst[i] - lst[i - 1]
    return max(lst)

print(result(vertical) * result(horizontal))