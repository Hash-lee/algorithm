t = int(input())
for i in range(t):
    n  = int(input())
    cases = list(map(int, input().split()))
    Mc = 0
    mc = 1000001
    for case in cases:
        if case > Mc:
            Mc = case
        if case < mc:
            mc = case
    r = Mc - mc
    
    print('#'+str(i+1),r)