import sys
sys.stdin = open('input_ladder.txt', 'r')

for _ in range(10):
    T = int(input())
    ladder = [[0] * 100 for _ in range(100)]

    for a in range(100):
        ladder[a] = list(map(int, input().split()))


    dx = [1, -1, 0]
    dy = [0, 0, 1]

    for r in range(100):
        x = r-1
        y = 0
        k = 0
        stop = 0

        if ladder[0][r] == 1:
            while True:
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < 100 and 0 <= ny < 100 and ladder[ny][nx] == 1:
                    x = nx
                    y = ny
                    ladder[ny][nx] = -1
                    if k == 2:
                        k = (k + 1) % 3

                elif 0 <= nx < 100 and 0 <= ny < 100 and ladder[ny][nx] == 2:
                    print('#{} {}'.format(T, r))
                    stop = 1
                    break

                elif ny == 100:
                    for i in range(100):
                        for j in range(100):
                            if ladder[i][j] == -1:
                                ladder[i][j] = 1
                    break
                else:
                    k = (k + 1) % 3
                    
        if stop:
            break