import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def check(arr):
    blue_or_white = arr[0][0]
    for one in arr:
        if sum(one) == blue_or_white * len(one):
            pass
        else:
            return False
    return True


def divide(arr):
    length = len(arr[0]) // 2
    arr_1 = [arr[r][:length] for r in range(length)]
    arr_2 = [arr[r][length:] for r in range(length)]
    arr_3 = [arr[r + length][:length] for r in range(length)]
    arr_4 = [arr[r + length][length:] for r in range(length)]
    return arr_1, arr_2, arr_3, arr_4


waiting = [arr]
checked = []

while waiting:
    target = waiting.pop(0)
    if check(target):
        checked.append(target)
    else:
        arr_1, arr_2, arr_3, arr_4 = divide(target)
        waiting.append(arr_1)
        waiting.append(arr_2)
        waiting.append(arr_3)
        waiting.append(arr_4)

white = 0
blue = 0
for paper in checked:
    if paper[0][0] == 1:
        blue += 1
    else:
        white += 1

print(white)
print(blue)