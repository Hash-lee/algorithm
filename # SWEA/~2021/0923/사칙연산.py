import sys
sys.stdin = open('사칙연산.txt', 'r')


def cal(a, b, x):
    if x == '+': return a+b
    elif x == '-': return a-b
    elif x == '/': return a/b
    elif x == '*': return a*b

def tree(n):
    global N
    for i in range(N+1):
        if arr[n][i] == 1:
            tree(i)
    l.append(nodes[n])


for t in range(1, 11):
    N = int(input())
    nodes = [0] * (N+1)
    arr = [[0] * (N+1) for _ in range(N + 1)]
    for n in range(N):
        lst = input().split()
        if len(lst)>2:
            arr[int(lst[0])][int(lst[2])] = 1
            arr[int(lst[0])][int(lst[3])] = 1
        try:
            nodes[int(lst[0])] = int(lst[1])
        except:
            nodes[int(lst[0])] = lst[1]

    l = []
    tree(1)

    g = ['+', '-', '/', '*']
    while len(l) > 1:
        for i in range(2, len(l)):
            if l[i] in g:
                a = l.pop(i-2)
                b = l.pop(i-2)
                x = l[i-2]
                l[i-2] = cal(a, b, x)
                break

    print('#{} {}'.format(t, int(l[0])))