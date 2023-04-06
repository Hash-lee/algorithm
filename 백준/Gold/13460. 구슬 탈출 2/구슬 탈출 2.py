import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = list(map(lambda x: list(x.strip()), sys.stdin.readlines()))
mn = 11

for r in range(N):
    for c in range(M):
        if arr[r][c] == "R":
            red = [r, c]
            arr[r][c] = "."
        if arr[r][c] == "B":
            blue = [r, c]
            arr[r][c] = "."
        if arr[r][c] == "O":
            hole = [r, c]

Q = deque([(red, blue)])
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
visit = {}


def promise(red, blue, k, check):
    check_red = not check and (arr[red[0] + dr[k]][red[1] + dc[k]] == "." or arr[red[0] + dr[k]][red[1] + dc[k]] == "O")
    check_blue = arr[blue[0] + dr[k]][blue[1] + dc[k]] == "." or arr[blue[0] + dr[k]][blue[1] + dc[k]] == "O"
    return check_red or check_blue


for iter in range(1, 11):
    for __ in range(len(Q)):
        red, blue = Q.popleft()
        for k in range(4):
            arr[red[0]][red[1]], arr[blue[0]][blue[1]] = "R", "B"
            nred, nblue = red[:], blue[:]
            check = 0
            while promise(nred, nblue, k, check):
                rr, rc = nred[0], nred[1]
                br, bc = nblue[0], nblue[1]
                nrr, nrc = nred[0] + dr[k], nred[1] + dc[k]
                nbr, nbc = nblue[0] + dr[k], nblue[1] + dc[k]
                if check == 0 and arr[nrr][nrc] == ".":
                    arr[rr][rc], arr[nrr][nrc] = arr[nrr][nrc], arr[rr][rc]
                    nred[0], nred[1] = nrr, nrc
                if arr[nbr][nbc] == ".":
                    arr[br][bc], arr[nbr][nbc] = arr[nbr][nbc], arr[br][bc]
                    nblue[0], nblue[1] = nbr, nbc
                if check == 0 and arr[nrr][nrc] == "O":
                    arr[rr][rc] = "."
                    check = iter
                if arr[nbr][nbc] == "O":
                    check = -1
                    break
            arr[nred[0]][nred[1]] = "."
            arr[nblue[0]][nblue[1]] = "."
            if 0 < check:
                print(check)
                exit()
            elif check == -1:
                continue
            else:
                if not visit.get(nred[0] * 1000 + nred[1] * 100 + nblue[0] * 10 + nblue[1], 0):
                    visit[nred[0] * 1000 + nred[1] * 100 + nblue[0] * 10 + nblue[1]] = 1
                    Q.append((nred, nblue))
print(-1)