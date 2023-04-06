import sys
sys.stdin = open('4865input.txt', 'r')



T = int(input())

for t in range(T):
    str1 = input()
    str2 = input()

    k = 0

    for a in str1:
        n = 0
        for b in str2:
            if a == b:
                n += 1
        if n > k:
            k = n

    print('#{} {}'.format(t+1, k))

