import sys

N = int(sys.stdin.readline())
arr_A = list(map(int, sys.stdin.readline().split()))
operator = dict(zip(["+", "-", "*", "/"], map(int, sys.stdin.readline().split())))

mn = 1000000001
mx = -1000000001


def DFS(num=arr_A[0], idx=1):
    if idx == N:
        global mn, mx
        if num < mn:
            mn = num
        if mx < num:
            mx = num
    else:
        cal = arr_A[idx]
        if operator["+"]:
            operator["+"] -= 1
            DFS(num + cal, idx + 1)
            operator["+"] += 1
        if operator["-"]:
            operator["-"] -= 1
            DFS(num - cal, idx + 1)
            operator["-"] += 1
        if operator["*"]:
            operator["*"] -= 1
            DFS(num * cal, idx + 1)
            operator["*"] += 1
        if operator["/"]:
            operator["/"] -= 1
            if num < 0:
                DFS(-((-num) // cal), idx + 1)
            else:
                DFS(num // cal, idx + 1)
            operator["/"] += 1


DFS()
print(mx)
print(mn)