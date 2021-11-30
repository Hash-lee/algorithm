def solution(orders, course):
    answer = []
    menu = [[] for _ in range(12)]
    comb = [[[], []] for _ in range(12)]

    # 주문 내역, 길이, 현재 인덱스, 선택메뉴, 메뉴 수
    def renual(sen, n, i=0, s='', k=0):
        # 완전탐색 종료 조건
        if i == n:
            if k > 1:
                # comb에 메뉴가 없다면 메뉴와 카운트 1 추가
                if not s in comb[k][0]: comb[k][0].append(s); comb[k][1].append(1)
                # 있다면 인덱스 찾아서 +1       # find? 로 바꾸면 더 깔끔할듯
                else: comb[k][1][comb[k][0].index(s)] += 1
        else:
            # 완전탐색하기
            renual(sen, n, i+1, s+sen[i], k+1)
            renual(sen, n, i+1, s, k)
    
    for order in orders:
        # 주문 순서 정렬
        order = "".join(sorted(":".join(order).split(":")))
        renual(order, len(order))

    # 2번 이상 주문된 메뉴에 대해 요구 조건에 맞는 메뉴 선정
    for k in range(course[-1]+2):
        com = comb[k]
        tmp = []
        mx = 2
        for i in range(len(com[1])):
            # 더 많이 주문한 메뉴가 나오면 리스트 초기화 및 변경
            if mx < com[1][i]:
                mx = com[1][i]
                tmp = [com[0][i]]
            # 주문 횟수가 같다면 append
            elif mx == com[1][i]:
                tmp.append(com[0][i])
        menu[k] = tmp

    # 코스에 있는 메뉴 수와 일치하는 메뉴 집어넣기
    for c in course:
        answer += menu[c]
    
    # 정렬순
    answer.sort()
    return answer