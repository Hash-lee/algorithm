R, C, M = map(int, input().split())
arr = [[0]*(C) for _ in range(R)]

def move(r, c, s, d, z, i):
    if d <= 2:
        v = s % ((R-1)*2)
        if d == 1:
            r = r - v
        elif d == 2:
            r = r + v
        while not 0 <= r < R:
            if d == 2:
                r = R - 1 - (r - R + 1)
                d = 1
            if r < 0:
                r = abs(r)
                d = 2
    else:
        v = s % ((C-1)*2)
        if d == 4:
            c = c - v
        elif d == 3:
            c = c + v
        while not 0 <= c < C:
            if d == 3:
                c = C - 1 - (c - C + 1)
                d = 4
            if c < 0:
                c = abs(c)
                d = 3

    if z < arr[r][c]:
        sharks[i] = 0
    else:
        sharks[i] = (r, c, s, d, z)
        arr[r][c] = z


def move_all():
    global arr
    arr = [[0]*(C) for _ in range(R)]
    for i in range(len(sharks)):
        if sharks[i]:
            r, c, s, d, z = sharks[i]
            move(r, c, s, d, z, i)



sharks = [list(map(int, input().split())) for _ in range(M)]
for i in range(len(sharks)):
    sharks[i] = (sharks[i][0] - 1, sharks[i][1] -1, sharks[i][2], sharks[i][3], sharks[i][4])
    r, c, s, d, z = sharks[i]

    arr[r][c] = z

sharks = sorted(sharks, key = lambda x: x[4], reverse=True)


fish = 0

for c in range(C):
    for r in range(R):
        if arr[r][c]:
            z = arr[r][c]
            for i in range(len(sharks)):
                if sharks[i] and sharks[i][4] == z:
                    sharks[i] = 0
                    break
            fish += z
            break
    move_all()

print(fish)