import sys
sys.stdin = open('괄호검사.txt', 'r')

def par(sen):
    l = [0] * len(sen)
    i = 0
    for s in sen:
        if s == '{' or s == '(':
            l[i] = s
            i += 1
        elif s == '}' or s == ')':
            i -= 1
            if (s == '}' and l[i] == '{') or (s == ')' and l[i] == '('):
                l[i] = 1
            else:
                return 0
    for w in l:
        if w == 1:
            return 1
        elif w == '{' or w == '(':
            return 0

T = int(input())

for t in range(1, T+1):
    sen = input()

    if par(sen):
        print('#{} {}'.format(t, 1))
    else: print('#{} {}'.format(t, 0))