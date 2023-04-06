def DFS(arr, num, L, loc, move):
    if num == 0:
        return move
    else:
        temp = []
        for i in range(L):
            des = (loc + i) % L
            if arr[des]:
                arr[des] = 0
                temp.append(DFS(arr, num-1, L, des, move + i))
                arr[des] = 1
                break
        for i in range(1, L):
            des = (L + loc - i) % L
            if arr[des]:
                arr[des] = 0
                temp.append(DFS(arr, num-1, L, des, move + i))
                arr[des] = 1
                break
        return min(temp)

def solution(name):
    d = {chr(i): i - 65 if i - 65 < 14 else 26 % (i - 65) for i in range(65, 91)}
    changes = list(map(lambda x: d[x], list(name)))
    visit = list(map(lambda x: 1 if x else 0, changes))
    work = sum(visit)
    L = len(name)
    return sum(changes) + DFS(visit, work, L, 0, 0)


print(solution("AABAAAAABBBBB"))