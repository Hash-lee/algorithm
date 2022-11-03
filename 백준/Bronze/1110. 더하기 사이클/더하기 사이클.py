import sys

N = sys.stdin.readline().rstrip()

number = N
count = 0
while True:
    count += 1
    if len(number) == 1:
        number = str(int(number + number))
    else:
        left, right = map(int, (" ".join(number)).split())
        add_num = str(left + right)
        number = str(int(str(right) + add_num[-1]))
    if number == N:
        break
print(count)
