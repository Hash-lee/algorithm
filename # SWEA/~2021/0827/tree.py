V = 13
arr = list(map(int, '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'.split()))
E = len(arr)//2

L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)

for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i +1]
    if L[p] == -:
        L[p] = c
    else:
        R[p] = c
    P[c] = p

def inorder(v):

    if L[v] == 0 and R[v] == 0:

    inorder(L[v])
    inorder(R[v])

