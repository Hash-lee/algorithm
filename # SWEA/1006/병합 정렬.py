import sys, time
sys.stdin = open('sample.txt', 'r')

def agr(lst):
    n = len(lst)
    if n == 1: return lst
    n = n//2
    left = agr(lst[:n])
    right = agr(lst[n:])
    return merge(left, right)

def merge(left, right):
    tmp = []
    global answer
    f1 = -1
    f2 = -1
    r1 = len(left) -1
    r2 = len(right) -1

    if left[r1] > right[r2]: answer += 1

    while f1 != r1 and f2 != r2:
        if left[f1+1] < right[f2+1]:
            f1 += 1
            tmp.append(left[f1])
        else:
            f2 += 1
            tmp.append(right[f2])

    while f1 != r1:
        f1 += 1
        tmp.append(left[f1])
        
    while f2 != r2:
        f2 += 1
        tmp.append(right[f2])
    return tmp


T = int(input())
for tc in range(1, T+1):
    answer = 0
    N = int(input())
    lst = list(map(int, input().split()))
    lst = agr(lst)

    print('#{} {} {}'.format(tc, lst[len(lst)//2], answer))