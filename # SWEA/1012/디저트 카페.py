import sys
sys.stdin = open('sample.txt', 'r')


dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]


def square(R, C, r, c, n=0, s=''):
    s += str(arr[r][c]) + " "
    if n == 4: return
    nr = r + dr[n]
    nc = c + dc[n]
    if nr == R:
        if nc == C and not s in lst:
            lst.append(s)
    else:
        if R <= nr < N  and 0 <= nc < N:
            square(R, C, nr, nc, n, s)
            square(R, C, nr, nc, n+1, s)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]

    answer = -1
    for r in range(N-1):
        for c in range(1, N-1):
            lst = []
            square(r, c, r, c)
            while lst:
                sqr = list(map(int, (lst.pop()).split()))
                flag = 1
                cnt = 0
                for s in sqr:
                    if sqr.count(s) > 1: flag = 0; break
                    else: cnt += 1
                if flag:
                    if cnt > answer:
                        answer = cnt
    
    print('#{} {}'.format(tc, answer))

