import sys
sys.stdin = open('sample.txt', 'r')

def inorder(n):
    if arr[n][1] == 0: return
    else:
        inorder(arr[n][2])
        string.append(arr[n][1])
        inorder(arr[n][3])

for t in range(1, 11):
    N = int(input())
    arr = [[0] * 4 for _ in range(N + 1)]
    string = []
    for i in range (1,N + 1):
         node = list(input().split())
         for j in range(len(node)):
            try: arr[i][j] = int(node[j])
            except: arr[i][j] = node[j]

    inorder(1)
    print('#{} {}'.format(t, "".join(string)))
