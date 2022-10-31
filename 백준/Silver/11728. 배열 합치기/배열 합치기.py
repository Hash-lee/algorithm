import sys

N, M = map(int, sys.stdin.readline().split())
arr_A = list(map(int, sys.stdin.readline().split()))
arr_B = list(map(int, sys.stdin.readline().split()))

fA, fB = 0, 0
while fA < N and fB < M:
    if arr_A[fA] < arr_B[fB]:
        print(arr_A[fA], end=" ")
        fA += 1
    else:
        print(arr_B[fB], end=" ")
        fB += 1

if fA < N:
    print(" ".join(list(map(str, arr_A[fA:]))))
if fB < M:
    print(" ".join(list(map(str, arr_B[fB:]))))