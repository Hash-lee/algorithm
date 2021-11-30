import sys
sys.stdin = open('pal.txt', 'r')



for t in range(10):
    arr = [0] * 100
    tc = input()
    for i in range(100):
        arr[i] = input()

    result = 0
    for n in range(100):
        m = 100 - n
        if result >= m:
            break
        for r in range(100):
            for c in range(n + 1):
                if result >= m:
                    break
                k = 0
                for x in range(m//2):
                    if arr[r][c + x] == arr[r][c + m -1 - x]:
                        k += 1
                    else:
                        break
                if k == m//2:
                    result = m

    for n in range(100):
        m = 100 - n
        if result >= m:
            break
        for c in range(100):
            for r in range(n + 1):
                if result >= m:
                    break
                k = 0
                for y in range(m//2):
                    if arr[r + y][c] == arr[r + m - 1 - y][c]:
                        k += 1
                    else:
                        break
                if k == m//2:
                    result = m

    print('#{} {}'.format(t+1, result))