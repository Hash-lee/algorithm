import sys
sys.stdin = open('반복문자 지우기.txt', 'r')

T = int(input())

def dlt(sen):
    ls = len(sen)
    if ls < 2:
        return ls
    for i in range(ls-1):
        if sen[i] == sen [i+1]:
            for j in range(i, ls-2):
                sen[j] = sen[j+2]
            return dlt(sen[:-2])
    return ls


for t in range(1, T+1):
    sen = list(input())
    print('#{} {}'.format(t, dlt(sen)))



