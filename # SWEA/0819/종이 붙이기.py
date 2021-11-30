import sys
sys.stdin = open('종이 붙이기.txt', 'r')

T = int(input())

def comb(a, b, c):
    m = 1
    n = 1
    for i in range(a, 0, -1):
        m *= i
    for j in range(b,0,-1):
        n *= j
    for k in range(c,0, -1):
        n *= k
    return m//n

def paper(N):
    k = N // 20
    l = N // 10
    result = 1

    for i in range(1, k+1):
        result += (comb(l - i, i,l - i*2) * (2**i))
    return result

for t in range(1, T+1):
    n = int(input())
    print('#{} {}'.format(t, paper(n)))