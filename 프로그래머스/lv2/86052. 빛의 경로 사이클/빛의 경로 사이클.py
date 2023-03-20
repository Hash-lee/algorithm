def solution(grid):
    answer = []
    w = len(grid[0])
    h = len(grid)

    visited = [[[0] * 4 for _ in range(len(grid[0]))] for __ in range(len(grid))]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for ir in range(h):
        for ic in range(w):
            for k in range(4):
                if visited[ir][ic][k] == 0:
                    Q = [(ir, ic, k)]
                    while Q:
                        r, c, d = Q.pop()
                        nr, nc, nd = (h + r + dr[d]) % h, (w + c + dc[d]) % w, d
                        if grid[nr][nc] == "L":
                            nd = (d + 3) % 4
                        if grid[nr][nc] == "R":
                            nd = (d + 1) % 4
                        if visited[nr][nc][nd]:
                            answer.append(visited[r][c][d])
                        else:
                            visited[nr][nc][nd] = visited[r][c][d] + 1
                            Q.append((nr, nc, nd))
    answer.sort()
    return answer
