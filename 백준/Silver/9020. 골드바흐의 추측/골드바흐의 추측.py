import sys

T = int(sys.stdin.readline())
for tc in range(T):
    N = int(sys.stdin.readline())
    if N == 4:
        print(2, 2)
        continue
    n, m = N // 2, N // 2
    while m > 1:
        m_cert, n_cert = True, True

        for i in range(2, n):
            if not n % i:
                n_cert = False
                break
            if i < m:
                if not m % i:
                    m_cert = False
                    break
        if m_cert and n_cert:
            print(m, n)
            break
        n += 1
        m -= 1