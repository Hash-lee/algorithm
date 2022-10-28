import sys

year = int(sys.stdin.readline())
if not year % 4:
    if year % 100 or not year % 400:
        print("1")
    else:
        print("0")
else:
    print("0")