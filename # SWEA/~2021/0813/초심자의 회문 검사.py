'''
#문자열 뒤집기
T = int(input())

for t in range(T):
    text = input()
    rtext = text[::-1]

    if text == rtext:
        print('#{} {}'.format(t+1, 1))
    else:
        print('#{} {}'.format(t + 1, 0))

'''
#교환을 통해 뒤집기

T = int(input())

for t in range(T):
    arr = list(input())
    N = len(arr)
    rev = [0] * N

    for i in range(N // 2):
        rev[i], rev[N - 1 - i] = arr[N - 1 - i], arr[i]

    if arr == rev:
        print('#{} {}'.format(t + 1, 1))
    else:
        print('#{} {}'.format(t + 1, 0))

        # 1 1
        # 2 0
        # 3 1
        # 4 0
        # 5 1
        # 6 0
        # 7 1
        # 8 0
        # 9 0
        # 10 1