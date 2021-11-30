dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(r, c, n, s):
    s += arr[r][c]
    if n == 1:
        if not s in chk:
            chk.append(s)
    else:
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < 4 and 0 <= nc < 4:
                global rear
                rear += 1
                Q[rear] = (nr, nc, n-1, s)

Q = [0] * 4096

T = int(input())
for tc in range(1, T+1):
    arr = [tuple(input().split()) for _ in range(4)]
    chk = []
    for r in range(4):
        for c in range(4):
            front = -1
            rear = 0
            Q[rear] = (r, c, 7, '')
            while front != rear:
                front += 1
                BFS(Q[front][0], Q[front][1], Q[front][2], Q[front][3])
    print('#{} {}'.format(tc, len(chk)))