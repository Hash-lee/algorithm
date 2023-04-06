# 프로그래머스도 RecursionError 뜰 수 있음!!!!!!
def solution(number, k):
    L = len(number)
    answer = ""

    mx, mxi, w = "-1", -1, ""
    loc, res = 0, L - k
    while res:
        for idx in range(loc, L - res + 1):
            if mx < number[idx]:
                mx, mxi, w = number[idx], idx, number[idx]
            if mx == "9":
                break
        answer += w
        mx, mxi, w, loc, res = "-1", -1, "", mxi + 1, res - 1

    return answer
