import sys
sys.stdin = open('수영장.txt', 'r')


for t in range(1, int(input())+1):
    d, m , m3, y = map(int, input().split())
    plan = list(map(int, input().split())) + [0, 0]
    pay = [0] * 14
    for p in range(len(plan)):
        if plan[p] == 0:
            pay[p] == ''
        else:
            if plan[p] * d < m:
                pay[p] = plan[p] * d
            else: pay[p] = m
    f_pay = pay[:]
    r_pay = pay[:]

    for i in range(12):
        if f_pay[i] != 0:
            if f_pay[i] + f_pay[i+1] + f_pay[i+2] > m3:
                f_pay[i], f_pay[i+1], f_pay[i+2]= m3, 0, 0

    for i in range(13, 2, -1):
        if r_pay[i] != 0:
            if r_pay[i] + r_pay[i-1] + r_pay[i-2] > m3:
                r_pay[i], r_pay[i-1], r_pay[i-2]= m3, 0, 0
    
    if sum(r_pay) > sum(f_pay): pay = f_pay
    else: pay = r_pay
    answer = y


    if sum(pay) < y: answer = sum(pay)
    print('#{} {}'.format(t, answer))