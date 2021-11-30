import sys
sys.stdin = open('2진.txt', 'r')



for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    dic = {'3211':0, '2221':1, '2122':2, '1411':3, '1132':4, '1231':5, '1114':6, '1312':7, '1213':8,'3112':9}
    arr = ''
    for n in range(N):
        sen = input()
        if int(sen) > 0:
            arr = sen

    s = 0
    for i in range(len(arr)):
        if arr[i] == '1':
            s = i
    
    s -= 55
    c = []
    for i in range(s, s+56, 7):
        lst = [0] * 4
        idx = 0
        lst[idx] += 1
        for j in range(1, 7):
            if arr[i+j] != arr[i+j-1]: idx += 1
            lst[idx] += 1
        w = "".join(list(map(str, lst)))
        c.append(dic.get(w))
    
    vf = c[-1]
    for i in range(7):
        if (i+1) % 2: vf += c[i] * 3
        else: vf += c[i]
    
    if vf % 10: print('#{} 0'.format(t))
    else: print('#{} {}'.format(t, sum(c)))
