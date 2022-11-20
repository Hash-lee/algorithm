import sys

string = sys.stdin.readline().rstrip()

minus = string.split("-")
num = 0
try:
    num += sum(map(int, minus[0].split("+")))
    for i in range(1, len(minus)):
        num -= sum(map(int, minus[i].split("+")))
except:
    num = sum(map(int, string.split("+")))

print(num)