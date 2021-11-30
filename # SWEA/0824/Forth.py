T = int(input())

for t in range(1, T+1):
    forth = input().split()
    stk = []


    try:
        for f in forth:
            if f == '*':
                stk[-2] = stk[-2] * stk[-1]
                stk.pop()
            elif f == '/':
                stk[-2] = stk[-2] // stk[-1]
                stk.pop()
            elif f == '+':
                stk[-2] = stk[-2] + stk[-1]
                stk.pop()
            elif f == '-':
                stk[-2] = stk[-2] - stk[-1]
                stk.pop()
            elif f == '.':
                a = stk.pop()
                if stk:
                    print('#{} {}'.format(t, 'error'))
                else:
                    print('#{} {}'.format(t, a))
            else:
                stk.append(int(f))
    except:
        print('#{} {}'.format(t, 'error'))