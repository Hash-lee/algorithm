t = int(input())

for i in range(t):
    n = int(input())
    cards = input()
    num = list(range(10))
    cnt_num = [0] * 10

    for card in cards:
        cnt_num[int(card)] += 1

    mx_num = -1
    mx_cnt = -1
    idx = -1
    for j in range(len(cnt_num)):
        if cnt_num[j] > mx_cnt:
            mx_cnt = cnt_num[j]
            idx = j
            mx_num = num[j]
        elif cnt_num[j] == mx_cnt:
            if num[j] > mx_num:
                mx_cnt = cnt_num[j]
                mx_num = num[j]

    print('#{} {} {}'.format(i + 1, mx_num, mx_cnt))