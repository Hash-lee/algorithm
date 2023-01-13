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


words = sorted(list(set([sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline()))])), key=lambda x: (len(x), x))
for word in words:
    L = len(word)
    dct = {chr(i): 0 for i in range(97, 123)}
    for c in word:
        dct[c] += 1
    alps = sorted(set(word))
    DFS()