import sys
sys.stdin = open('sample_gns.txt', 'r')


num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())

for t in range(T):
    arr = [0] * 10
    tc, N = input().split()
    A = list(input().split())

    for i in range(10):
        for a in A:
            if num[i] == a:
                arr[i] += 1
    result = []
    for k in range(10):
        result += [num[k]] * arr[k]

    print(tc)
    print(" ".join(result))