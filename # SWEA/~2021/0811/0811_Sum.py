import sys
sys.stdin = open('sample_input.txt', 'r')

for i in range(10):
    test_num = int(input())
    arr = [[0] * 100 for _ in range(100)]
    result = 0

    for j in range(100):
        arr[j] = list(map(int, input().split()))

    lr_cross = 0
    rl_cross = 0

    for r in range(100):
        tmp_row_sum = 0

        for c in range(100):
            tmp_row_sum += arr[r][c]
            if r == c:
                lr_cross += arr[r][c]

        if tmp_row_sum > result:
            result = tmp_row_sum

    for c in range(100):
        tmp_col_sum = 0
        for r in range(100):
            tmp_col_sum += arr[r][c]
            if (99 - c) == r:
                rl_cross += arr[r][c]
        if tmp_col_sum > result:
            result = tmp_col_sum

    if lr_cross > result :
        result = lr_cross
    if rl_cross > result :
        result = rl_cross

    print('#{} {}'.format(i+1, result))