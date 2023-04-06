hexa = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
def bi(n, k):
    if k == 1: return str(n%2)
    else: return bi(n//2, k-1) + str(n%2)

for t in range(1, int(input())+1):
    N, M = input().split()
    answer = ''
    for i in range(int(N)):
        answer += bi(hexa.index(M[i]), 4)
    
    print('#{} {}'.format(t, answer))