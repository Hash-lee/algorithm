# 최대 진법에 대한 index 참고용
hexa = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

# 모든 수를 일렬로 붙여 리턴
def ex(mt, n):
    s = hexa[mt%n]
    if mt < n: return s
    else: return ex(mt//n, n) + s

def solution(n, t, m, p):
    word = ''
    for i in range(m*t):
        word += ex(i, n)

    # p번째 수 부터 인원간격으로 리턴
    answer = ''
    for j in range(p-1, m*t, m):
        answer += word[j]

    return answer




# 통과