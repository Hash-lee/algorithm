T = int(input())

def dec(lst, n):
    ten = 0
    k = 0
    for _ in range(len(lst)):
        ten += lst.pop() * (n ** k)
        k += 1
    return ten

for tc in range(1, T+1):
    two = []
    bi = list(map(int, (":".join(input())).split(":")))
    
    for i in range(len(bi)):
        bi[i] = (bi[i]+1) % 2
        two.append(bi[:])
        bi[i] = (bi[i]+1) % 2

    thr = []
    tri = list(map(int, (":".join(input())).split(":")))
    for i in range(len(tri)):
        for j in range(1, 3):
            tri[i] = (tri[i]+1)%3
            thr.append(tri[:])
        tri[i] = (tri[i]+1)%3

    check = []
    for sec in two:
        check.append(dec(sec, 2))
    
    for thi in thr:
        con = dec(thi, 3)
        if con in check:
            print('#{} {}'.format(tc, con))
            break