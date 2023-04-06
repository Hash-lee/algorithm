import sys
sys.stdin = open('sample3.txt', 'r')

def my_pop():
    global f, N
    f = f + 1
    return Oven[f]
def push(item):
    global N, r
    Oven.append(item)
    r = r + 1
def isEmpty():
    global f, r
    return f + 1 == r

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Pizza = list(range(1, M + 1))
    tmp = list(map(int, input().split()))
    Cheese = {}
    for i in range(1, M+1):
        Cheese[i] = tmp[i-1]
    Oven = []
    f = -1
    r = 0

    for _ in range(N):
        push(Pizza.pop(0))

    while not isEmpty():
        pz = my_pop()
        chz = Cheese[pz] // 2
        if chz:
            push(pz)
            Cheese[pz] = chz
        else:
            if Pizza: push(Pizza.pop(0))

    print('#{} {}'.format(t, Oven[-1]))