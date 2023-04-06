import sys
sys.stdin = open('이진탐색.txt', 'r')


T = int(input())

for t in range(T):
    P, A, B = map(int, input().split())

    def EZ(Search, end, start=1):
        center = int((end + start)/2)
        if center == Search:
            return 1
        elif Search in range(start, center):
            return 1 + EZ(Search, center, start)
        else:
            return 1 + EZ(Search, end, center)

    if EZ(A, P) < EZ(B, P) :
        print('#'+str(t+1),'A')
    elif EZ(A, P) > EZ(B, P) :
        print('#'+str(t+1),'B')
    else:
        print('#' + str(t+1), '0')