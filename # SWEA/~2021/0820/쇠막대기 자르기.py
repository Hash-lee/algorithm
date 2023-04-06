import sys
sys.stdin = open('s2.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    d = list(input())
    lt = len(d)
    x = 0

    for i in range(lt - 1):
        if d[i] == '(' and d[i + 1] == ')':
            d[i], d[i + 1] = 0, -1

    Id = 0
    cnt = 0
    for j in range(lt):
        if d[j] == '(':
            Id += 1
        elif d[j] == ')':
            Id -= 1
            cnt += 1
        elif d[j] == -1:
            x += Id

    print('#{} {}'.format(t, x + cnt))
