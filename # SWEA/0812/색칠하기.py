import sys
sys.stdin = open('color.txt', 'r')

T = int(input())

for t in range(T):
    C = int(input())
    arr = [[0] * 10 for _ in range(10)]
    p = 0

    for c in range(C):
        x1, y1, x2, y2, cc = map(int, input().split())

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if arr[y][x] == 3:
                    pass
                elif arr[y][x] == 0:
                    arr[y][x] = cc
                elif arr[y][x] != cc:
                    arr[y][x] = 3
                    p += 1
    print('#{} {}'.format(t+1,p))