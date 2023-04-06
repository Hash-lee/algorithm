from collections import deque


def solution(begin, target, words):
    L = len(words)
    l = len(begin)
    arr = [[0 for _ in range(L + 2)] for _ in range(L + 2)]
    tmp = [begin, target] + words

    for i in range(L):
        for j in range(i + 1, L + 1):
            cnt = 0
            for k in range(l):
                if tmp[i][k] == tmp[j][k]:
                    pass
                else:
                    cnt += 1
                    if cnt > 1:
                        break
            if cnt == 1:
                arr[i][j], arr[j][i] = 1, 1

    V = [0] * (L + 2)
    Q = deque([(0, 0)])
    brk = 1
    while Q and brk:
        idx, num = Q.popleft()
        for c in range(1, L + 2):
            if arr[idx][c] == 1 and V[c] == 0:
                V[c] = num + 1
                if c == 1:
                    brk = 0
                    break
                else:
                    Q.append((c, num + 1))
    answer = V[1]
    for a in arr:
        print(a)
    print("")
    print(V)

    return answer


print(solution("hit", "cog", ["hot", "d ", "dog", "lot", "log"]))

