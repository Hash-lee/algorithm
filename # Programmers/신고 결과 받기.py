def solution(id_list, report, k):
    num = {}
    L = len(id_list)
    for i in range(L):
        num[id_list[i]] = i
    
    answer = [0] * L
    V = [0] * L
    reports = set(report)

    for re in reports:
        s, e = re.split()
        V[num[e]] += 1
        
    for re in reports:
        s, e = re.split()
        if V[num[e]] >= k:
            answer[num[s]] += 1
    
    
    return answer