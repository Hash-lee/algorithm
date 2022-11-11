import sys

infos = list(map(int, sys.stdin.readline().split()))


needs = [0] * 20
holds = [0] * 20

for _ in range(int(sys.stdin.readline())):
    idx, num = map(int, sys.stdin.readline().split())
    holds[idx] = num

one_flag = True
for i in range(3):
    if infos[i] == 1:
        needs[0] = infos[i - 1] * infos[i - 2]
        one_flag = False
        break
    if infos[i] % 2:
        needs[0] += infos[i - 1] * infos[i - 2]
        infos[i] -= 1


def PutBigCube(arr, max_size=20):
    mn, md, mx = sorted(arr)
    big = 21
    for size in range(max_size, -1, -1):
        if 2**size <= mn:
            big = size
            break

    cube = 2**big
    mn_cube, md_cube, mx_cube = 1, md // cube, mx // cube
    res_mn, res_md, res_mx = mn % cube, md % cube, mx % cube
    needs[big] += mn_cube * md_cube * mx_cube

    if res_mx:
        PutBigCube([mn, md, res_mx], big - 1)
    if res_md:
        PutBigCube([mn, res_md, mx - res_mx], big - 1)
    if res_mn:
        PutBigCube([res_mn, md - res_md, mx - res_mx], big - 1)


if one_flag:
    PutBigCube(infos)
needs = needs[::-1]
holds = holds[::-1]

use_cube = 0
for i in range(20):
    if needs[i] <= holds[i]:
        use_cube += needs[i]
    else:
        if i == 19:
            use_cube = -1
            break
        use_cube += holds[i]
        needs[i + 1] += (needs[i] - holds[i]) * 8

print(use_cube)
