import sys


def DFS(s="", n=0):
    if n == L:
        print(s)
    else:
        for alp in alps:
            if dct[alp]:
                dct[alp] -= 1
                DFS(s + alp, n + 1)
                dct[alp] += 1


words = sorted((([sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline()))])), key=lambda x: (len(x), x))
for word in words:
    L = len(word)
    alps = sorted(set(word))
    dct = {alp: 0 for alp in alps}
    for c in word:
        dct[c] += 1
    DFS()