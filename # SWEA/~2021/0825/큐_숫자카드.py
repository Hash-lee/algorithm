T = int(input())

def push(item):
    global n, r
    r = (r + 1) % n
    Q[r] = item

def my_pop():
    global f, n
    f = (f + 1) % n
    return Q[f]

for t in range(1, T+1):
    f = r = 0
    n = int(input()) + 1
    Q = [0] * n
    for i in range(1, n):
        push(i)

    i = 1
    while f != r:
        if i: my_pop()
        else: push(my_pop())
        i = (i+1) % 2

    print('#{} {}'.format(t, Q[r]))