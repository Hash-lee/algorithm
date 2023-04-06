T = int(input())

def mid(a):
    if a == 1:
        return []
    result = []
    for k in range(a-1):
        result += [arr[a-1][k] + arr[a-1][k+1]]
    return result

for t in range(1,T+1):
    n = int(input())
    arr = [0] * n
    arr[0] = [1]
    if n > 1:
        for i in range(1, n):
                arr[i] = [1] + mid(i)  + [1]

    print('#'+str(t))
    for a in arr:
        print(" ".join(list(map(str, a))))






