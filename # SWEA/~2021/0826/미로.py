import sys
sys.stdin = open('sample4.txt', 'r')

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def BFS(y, x):
    global result
    if result: return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if miro[ny][nx] == 0 and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            BFS(ny, nx)
        elif miro[ny][nx] == 3:
            result = 1
            return

for tc in range(10):
    t = int(input())
    miro = [[0] * 16 for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    for r in range(16):
        num = input()
        for c in range(16):
            miro[r][c] = int(num[c])
            if num[c] == '2':
                sr, sc = r, c
    result = 0
    BFS(sr, sc)

    print('#{} {}'.format(t, result))