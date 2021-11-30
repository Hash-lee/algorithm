def push(item):
    global r, q
    r = (r+1) % q
    Q[r] = item
def my_pop():
    global f, q
    f = (f + 1) % q
    return Q[f]

for t in range(1):
    T = input()
    f = r = 0
    inQ = list(map(int, input().split()))
    q = len(inQ) + 1
    Q = [0] * q
    for iq in inQ:
        push(iq)

    k = list(range(1,6))
    i = 0
    while Q[r]:
        n = my_pop() -  k[i]

        if n <= 0:
            push(0)
        else: push(n)

        i = (i + 1) % 5


    print('#'+T, end = ' ')
    for _ in range(len(inQ)):
        print(my_pop(), end = ' ')



'''
for t in range(1):
    T = int(input())
    Q = list(map(int, input().split()))
    k = 0
    while Q[-1] > 0:
        Q.append(Q.pop(0) - ((k % 5) + 1))
        k += 1
        print(Q)
    Q[-1] = 0
    print(Q)


'''


'''
        for i in range(1, n+1):
            q = Q.pop(0) - i
            if q > 0:
                Q.append(q)
            else:
                Q.append(0)
                break
'''



