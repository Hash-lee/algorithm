for t in range(1,11):
    n = int(input())
    infix = input()

    icp = {"(": 3, "*": 2, "/": 2, "+": 1, "-": 1, ")": 3}
    isp = {"(": 0, "*": 2, "/": 2, "+": 1, "-": 1}

    stk = []

    postfix = []

    for s in infix:
        if s in icp:
            # 닫는 괄호일 때
            if s == ")":
                while stk[-1] != "(":
                    postfix.append(stk.pop())
                stk.pop()
            else:
                # 닫는 괄호가 아니고 내용물이 있다면?
                if stk:
                    if icp[s] > isp[stk[-1]]:
                        stk.append(s)
                    else:
                        while stk and icp[s] <= isp[stk[-1]]:
                            postfix.append(stk.pop())
                        stk.append(s)
                # 비었으면 그냥 넣기
                else:
                    stk.append(s)
        # 숫자는 그냥 in
        else:
            postfix.append(int(s))

    while stk:
        postfix.append(stk.pop())

    cal = []
    for p in postfix:
        if p == '*':
            cal.append(cal.pop() * cal.pop())
        elif p == '/':
            cal.append(cal.pop() / cal.pop())
        elif p == '+':
            cal.append(cal.pop() + cal.pop())
        elif p == '-':
            cal.append(cal.pop() - cal.pop())
        else:
            cal.append(p)
    print('#{} {}'.format(t, cal[0]))
