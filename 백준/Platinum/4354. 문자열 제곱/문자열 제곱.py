import sys

def answer(string, length):
    res = 1
    for i in range(length//2, 0, -1):
        if length % i: continue
        k = length // i
        standard = string[:i]
        code = 1
        for s in range(1, k):
            proof = string[s*i:(s+1)*i]
            if standard != proof:
                code = 0
                break
        if code:
            res *= answer(string[:i], i)
            return res * k
    return res


for _ in range(10):
    string = sys.stdin.readline().strip()
    if string == ".": break
    L = len(string)
    print(answer(string, L))