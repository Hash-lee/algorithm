def solution(msg):
    dic = ['/////']
    for i in range(65, 91):
        dic.append(chr(i))
    
    lm = len(msg)
    Q = [0] * lm
    f = 0
    r = -1

    for _ in range(lm):
        r += 1
        Q[r] = msg[r]

    answer = []
    if f == r:
        answer.append(dic.index(Q[f]))
    while f != r:
        w = Q[f]
        while f != r and w in dic:
            f += 1
            idx = dic.index(w)
            w += Q[f]
        l = 0
        if w in dic:
            idx = dic.index(w)
        else:
            if f == r:
                l = dic.index(Q[f])
        answer.append(idx)
        dic.append(w)
        if l: answer.append(l)

    return answer

print(solution('A'))