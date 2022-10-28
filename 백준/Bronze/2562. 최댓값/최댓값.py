import sys

mx = 1
mx_line = 1

y = 0
for line in sys.stdin.readlines():
    y += 1
    n = int(line)
    if n > mx:
        mx = n
        mx_line = y

print(mx)
print(mx_line)