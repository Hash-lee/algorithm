import sys

T = int(sys.stdin.readline())
for tc in range(T):
    N = int(sys.stdin.readline())
    visit = [1] * N
    vectors = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    vectors.sort(key=lambda x:x[0]**2 + x[1]**2)
    mn = float("INF")
    
    def check(idx=0, selected=0, s=[0, 0]):
        global mn
        if idx == N:
            if selected == N//2:
                mn = min(mn, (s[0]**2+s[1]**2)**.5)
        else:
            if selected < N//2 < N - idx + selected:
                check(idx+1, selected+1, [s[0]-vectors[idx][0], s[1]-vectors[idx][1]])
            check(idx+1, selected, [s[0]+vectors[idx][0], s[1]+vectors[idx][1]])
    check()
    print(f'{str(mn):08}')