import sys
sys.stdin = open('sample_3.txt', 'r')


T = int(input())

for tc in range(T):
    str1 = input()
    str2 = input()
    cnt = 0

    N = len(str1)
    M = len(str2)

    for m in range(M-N+1):
        if str2[m] == str1[0]:
            tmp = 1
            for n in range(1, N):
                if str2[m+n] != str1[n]:
                    break
                else: tmp += 1
            if tmp == N:
                cnt += 1

    print('#{} {}'.format(tc+1, cnt))