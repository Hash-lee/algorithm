def solution(k, tangerine):
    dic = {}
    for tan in tangerine:
        dic[tan] = dic[tan] + 1 if dic.get(tan, 0) else 1
    lst = sorted(dic.values(), reverse=True)
    answer = 0
    while 0 < k:
        k -= lst[answer]
        answer += 1
    return answer