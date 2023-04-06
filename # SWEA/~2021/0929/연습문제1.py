sen = '0000000111100000011000000111100110000110000111100111100111111001100111'

idx = 0
while len(sen) > idx:
    p = sen[idx:idx+7]
    num = 0
    for i in range(len(p)):
        num += (2**(6-i)) * int(p[i])
        # if p[i] == '1':               비트 연산자
        #    num |=1 << (6-i)
    print(num, end = ' ')
    idx += 7