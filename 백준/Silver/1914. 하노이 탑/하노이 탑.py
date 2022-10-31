import sys

N = int(sys.stdin.readline())


def hanoi(plate, dep, des):
    if plate == 0:
        return
    else:
        new_dep = 6 - dep - des
        hanoi(plate - 1, dep, new_dep)
        print(f"{dep} {des}")
        hanoi(plate - 1, new_dep, des)


print(2**N - 1)
if N <= 20:
    hanoi(N, 1, 3)