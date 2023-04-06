import sys
sys.stdin = open('암호코드스캔.txt', 'r')

hexa = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
dic = {(2, 1, 1) : 0, (2, 2, 1) : 1, (1, 2, 2) : 2, (4, 1, 1) : 3, (1, 3, 2) : 4, (2, 3, 1) : 5, (1, 1, 4) : 6, (3, 1, 2) : 7, (2, 1, 3) : 8, (1, 1, 2) : 9}

def bi(n, k):
    if k == 1: return str(n%2)
    else: return bi(n//2, k-1) + str(n%2)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    arr = list(set(arr))

    codes = []
    for i in range(len(arr)):    
        if arr[i] != '0'*M:
            code = ''
            for j in range(M):
                code += bi(hexa.index(arr[i][j]), 4)
            codes.append(code)
    
    nums = []
    for code in codes:
        tmp = []
        lst = [0]
        idx = 0
        lst[idx] += 1
        for i in range(1, len(code)):
            if code[i] != code[i-1]:
                lst.append(0)
                idx +=1
            lst[idx] += 1
        for j in range(0, len(lst)-3, 4):
            mn = 999
            for k in range(1,4):
                if mn > lst[j+k]: mn = lst[j+k]
            tu = (lst[j+1]//mn, lst[j+2]//mn, lst[j+3]//mn)
            if tu in dic:
                tmp.append(dic[tu])
        while tmp:
            sl = tmp[:8]
            if not sl in nums:
                nums.append(sl)
            tmp = tmp[8:]
    
    answer = 0
    for num in nums:
        n = num[-1]
        for l in range(7):
            if (l+1) % 2: n += num[l] * 3
            else: n += num[l]
        if not n % 10: answer += sum(num)
    
    print('#{} {}'.format(t, answer))
