import sys
sys.stdin = open('s3.txt', 'r')


T = int(input())

for t in range(1, T+1):
    arr = [[-1] * 5 for _ in range(15)]
    for i in range(5):
        sen = input()
        for j in range(len(sen)):
            arr[j][i] = sen[j]

    s = []
    for a in arr:
        for x in range(5):
            if a[x] != -1:
                s += [a[x]]
    print('#{} {}'.format(t, "".join(s)))