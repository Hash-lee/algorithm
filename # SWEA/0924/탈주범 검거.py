import sys
sys.stdin = open('탈주범 검거.txt', 'r')

left = [1, 3, 6, 7]
right = [1, 3, 4, 5]
up = [1, 2, 4, 7]
down = [1, 2, 5, 6]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def move(r, c, h):
    if h == 0: return
    check[r][c] = h
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and check[nr][nc] < h:
            if i == 0 and arr[r][c] in right and arr[nr][nc] in left:
                move(nr, nc, h-1)
            if i == 1 and arr[r][c] in down and arr[nr][nc] in up:
                move(nr, nc, h-1)
            if i == 2 and arr[r][c] in left and arr[nr][nc] in right:
                move(nr, nc, h-1)
            if i == 3 and arr[r][c] in up and arr[nr][nc] in down:
                move(nr, nc, h-1)



T = int(input())
for t in range(1, T+1):
    n, m, r, c, h = list(map(int, input().split()))
    arr = [0] * n
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    check = [[0] * m for _ in range(n)]
    move(r, c, h)
    
    answer = 0
    for x in check:
        for y in x:
            if y != 0:
                answer += 1
    
    print('#{} {}'.format(t, answer))
