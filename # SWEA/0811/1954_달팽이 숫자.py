# 효율 어ㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅁ청 낮은듯
def shell(d, n = 0, init = 0):
    #d : 변 길이 n : 수행횟수 init : 시행 초기값
    for i in range(n, d):
        for j in range(n, d):
            if i == n:
                arr[i][j] = init + j + 1 - n
            elif j == d - 1:
                arr[i][j] = init * 2 + d + i - n
            elif i == d - 1:
                arr[i][j] = init + d * 3 - j - n * 2 - 2
            elif j == n:
                arr[i][j] = init + d * 4 - i - n * 3 - 3
    if d - n > 1:
        return shell(d-1, n+1, arr[n+1][n])
    else:
        return arr

T = int(input())

for i in range(T):
    N = int(input())
    print('#'+str(i+1))
    arr = [[0] * N for _ in range(N)]
    shell(N)
    for ar in arr:
        print(" ".join(list(map(str, ar))))

'''
# 온라인 강의 풀이

T = int(input())
for t in range(T):
    N = int(input())
    A = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 0
    cnt = 1
    i, j = 0, -1
    while cnt <= N**2:
        ni, nj = i + di[k], j + dj[k]
        if (0 <= ni < N) and (0 <= nj < N) and (A[ni][nj] ==0):
            A[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            k = (k + 1) % 4

    print('#{}'.format(t+1))

    for a in A:
        print(" ".join(list(map(str, a))))
'''