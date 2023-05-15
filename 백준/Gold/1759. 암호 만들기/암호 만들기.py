mo = ('a', 'e', 'i', 'o', 'u')

L, C = map(int, input().split())
alp = input().split()
alp.sort()

def pw(idx=0, n=0, a=0, b=0, s=''):
    if n == L:
        if 0 < a and 1 < b:
            print(s)
    else:
        for i in range(idx, C):
            if alp[i] in mo:
                pw(i+1,n+1, a+1, b, s+str(alp[i]))
            else:
                pw(i+1,n+1, a, b+1, s+str(alp[i]))

pw()