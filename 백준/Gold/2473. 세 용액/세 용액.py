import sys
N = int(sys.stdin.readline())
solutions = sorted(map(int, sys.stdin.readline().split()))
mn = float("INF")
comb = ""

def binary(s, l, r=N):
    mn = float("INF")
    m_idx = -1

    while l < r:
        i = (l + r) // 2
        m = solutions[i]
        if abs(s + m) < mn:
            m_idx = i
            mn = abs(s + m)
        
        if s + m == 0:
            return i, 0
        elif 0 < s + m:
            r = i
        else:
            l = i + 1
    return m_idx, mn


for s1 in range(N-2):
    for s2 in range(s1+1, N-1):
        s3, temp = binary(solutions[s1] + solutions[s2], s2+1)
        if temp < mn:
            mn = temp
            comb = (solutions[s1], solutions[s2], solutions[s3])

print(*comb)