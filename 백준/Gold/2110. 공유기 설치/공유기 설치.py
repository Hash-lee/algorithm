import sys

sys.setrecursionlimit(10**6)

N, C = map(int, sys.stdin.readline().split())
arr = sorted([int(n) for n in sys.stdin.readlines()])


def Promise(array, distance, router, idx=0):
    if router:
        if idx == 0:
            return Promise(array, distance, router - 1, idx + 1)
        else:
            for i in range(idx, N - router + 1):
                if distance <= arr[i] - arr[idx - 1]:
                    return Promise(array, distance, router - 1, i + 1)
            return False
    else:
        return True


s = 0
e = max(arr)
while s <= e:
    distance = (s + e) // 2
    cert = Promise(arr, distance, C)
    # print(s, e, distance, cert)
    if cert:
        s = distance + 1
    else:
        e = distance - 1
print((s + e) // 2)