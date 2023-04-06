import sys
sys.stdin = open('sample.txt', 'r')

def cal(a, b):
    tmp = [a+1, a-1, a*2, a-10]
    for t in tmp:
        if 0 < t <= 1000000 and (V[t]==0 or V[t] > V[a] +1):
            V[t] = V[a] + 1
            global rear
            rear += 1
            Q[rear] = t


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    V = [0] * 1000001
    Q = [0] * 1000001
    front = -1
    rear = 0
    Q[rear] = N
    V[N] = 1
    
    while front != rear:
        front += 1
        if Q[front] > 1000000: continue
        elif Q[front] == M: break
        cal(Q[front], V[Q[front]])

    print('#{} {}'.format(tc, V[M]-1))