import sys

K = int(sys.stdin.readline())
for tc in range(K):
    V, E = map(int, sys.stdin.readline().split())
    visit = [1] * (V + 1)
    color_codes = [""] * (V + 1)
    edges = {}
    for _ in range(E):
        p1, p2 = map(int, sys.stdin.readline().split())
        try:
            edges[p1].append(p2)
        except:
            edges[p1] = [p2]
        try:
            edges[p2].append(p1)
        except:
            edges[p2] = [p1]

    Q = [0] * V
    front = -1
    rear = -1

    flag = True
    for vortex in range(1, V + 1):
        if visit[vortex]:
            if not edges.get(vortex):
                continue
            rear += 1
            Q[rear] = vortex
            visit[vortex] = 0
            color_codes[vortex] = "WHITE"

            while front < rear:
                front += 1
                start = Q[front]
                color = "WHITE" if color_codes[start] == "BLACK" else "BLACK"
                for end in edges[start]:
                    if visit[end]:
                        visit[end] = 0
                        rear += 1
                        Q[rear] = end
                        color_codes[end] = color
                    else:
                        if color_codes[end] != color:
                            flag = False
                            break
                if not flag:
                    break
        if not flag:
            break
    if flag:
        print("YES")
    else:
        print("NO")