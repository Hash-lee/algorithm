sen = '416A676F725974684D2050726F626C656D20536F6C76696E6'



idx = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')

def bi(num, n):
    if n == 1: return '0'
    if num % 2: return bi(num//2, n-1) + '1'
    else: return bi(num//2, n-1) + '0'

con_sen = ''
for s in sen:
    con_sen += bi(idx.index(s), 4)

for i in range(0, len(con_sen), 7):
    num = 0
    for j in range(7):
        if con_sen[i+j] == '1':
            num |=1 << (6-j)
    print(num, end=' ')