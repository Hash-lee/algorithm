import sys
sys.stdin = open('어디에 단어가 들어갈 수 있을까.txt', 'r')


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    arr = [0] * N
    for n in range(N):
        arr[n] = list(map(int, input().split()))

    cnt_x = 0
    cnt_y = 0

    for y in range(N):
        for x in range(N):
            if (x == 0 or (x > 0 and arr[y][x-1] == 0)) and (arr[y][x] == 1):
                now_w = 1
                f = 1
                while x + f < N and arr[y][x+f] == 1:
                    now_w += 1
                    f += 1
                if now_w == K:
                    cnt_x += 1

    for x in range(N):
        for y in range(N):
            if (y == 0 or (y > 0 and arr[y-1][x] == 0)) and (arr[y][x] == 1):
                now_h = 1
                f = 1
                while y + f < N and arr[y+f][x] == 1:
                    now_h += 1
                    f += 1

                if now_h == K:
                    cnt_y += 1


    print('#{} {}'.format(t+1,cnt_x+cnt_y))