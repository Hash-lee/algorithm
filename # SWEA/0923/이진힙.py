import sys
sys.stdin = open('이진힙.txt', 'r')


def heap(lst):
    for i in range(len(lst)):
        arr.append(lst[i])
        n = i+1
        while n >= 2:
            if arr[n] < arr[n//2]:
                arr[n], arr[n//2] = arr[n//2], arr[n]
            n = n//2

def sum_tree(n):
    if n == 1: return arr[1]
    else:
        if n % 2: return arr[n] + sum_tree((n - 1)//2)
        else: return arr[n] + sum_tree(n//2)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [0]
    lst = list(map(int, input().split()))
    heap(lst)
    print('#{} {}'.format(t, sum_tree(N)-arr[N]))
