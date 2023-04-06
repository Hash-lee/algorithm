import sys
sys.stdin = open('s7.txt', 'r')

T = int(input())

def rot(arr, n):
    result = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            result[r][c] = arr[-c-1][r]
    return  result

for t in range(1, T + 1):
    N = int(input())
    arr = [0] * N
    for n in range(N):
        arr[n] = list(input().split())

    arr90 = rot(arr, N)
    arr180 = rot(rot(arr, N), N)
    arr270 = rot(rot(rot(arr, N), N), N)

    print('#'+str(t))
    for i in range(N):
        print("".join(arr90[i]), "".join(arr180[i]), "".join(arr270[i]))