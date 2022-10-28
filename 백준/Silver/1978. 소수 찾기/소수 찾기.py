import sys
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

count = 0
for number in numbers:
    if number == 2:
        count += 1
    elif number > 1:
        bl = True
        for i in range(2, number):
            if not number % i:
                bl = False
                break
        if bl:
            count += 1
print(count)