import sys

N, M = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)


def wood(array, height):
    result = 0
    for one in array:
        if height < one:
            result += one - height
        else:
            break
    return result


pl = 0
pr = max(arr)
height = -1
if M <= 1:
    print(pr - M)
else:
    while pl < pr:
        height = (pl + pr) // 2
        acq = wood(arr, height)
        #print(height, acq, pl, pr)
        if acq < M:
            pr = height
        elif M <= acq:
            if pl + 1 == pr:
                break
            pl = height
    print(height)