import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

number_string = [str(i) for i in range(10)]

blank = []

last = False
for s in S:
    if s in number_string:
        if last:
            blank[-1].append(s)
        else:
            blank.append([s])
        last = True
    else:
        last = False

result = 0
for b in blank:
    result += int("".join(b))
print(result)