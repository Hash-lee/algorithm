import sys
sys.stdin = open('sample.txt', 'r')

def srt(n='', a = 0):
    if len(n) == N:
        if sum(list(map(int, (":".join(n)).split(":")))) == N//2:
            lst.append(n)
    else:
        for i in range(2):
            srt(n+str(i))

for tc in range(1, int(input())+1):
    N = int(input())
    S = [tuple(map(int, input().split())) for _ in range(N)]
    lst = []
    srt()

    answer = 99999999999999

    for p in lst:
        Sa = Sb = 0
        La = []
        Lb = []
        for n in range(N):
            if p[n] == '1': La.append(n)
            else: Lb.append(n)

        for i in range(N//2):
            for j in range(N//2):
                if i != j:
                    Sa += S[La[i]][La[j]]
                    Sb += S[Lb[i]][Lb[j]]

        if abs(Sa-Sb) < answer: answer = abs(Sa-Sb)

    print('#{} {}'.format(tc, answer))