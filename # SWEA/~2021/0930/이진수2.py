for t in range(1, int(input())+1):
    num = float(input())

    s = ''
    x = -1
    while num != 0 and x > -13:
        if num >= 2**x:
            s += '1'
            num -= 2**x
        else: s+='0'
        x -= 1
    if num != 0: s='overflow'

    print('#{} {}'.format(t, s))



