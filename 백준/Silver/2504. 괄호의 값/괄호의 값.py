import sys

prt = sys.stdin.readline().strip()

stck = []
points = 0
mul = 1
left = ["(", "["]
right = [")", "]"]
flag = False
for s in prt:
    if s == "(":
        stck.append(s)
        mul *= 2
        flag = True
    elif s == "[":
        stck.append(s)
        mul *= 3
        flag = True
    elif s in right:
        if not stck:
            points = 0
            break
        if s == ")":
            if stck.pop() != "(":
                points = 0
                break
            if flag:
                points += mul
                flag = False
            mul //= 2
        elif s == "]":
            if stck.pop() != "[":
                points = 0
                break
            if flag:
                points += mul
                flag = False
            mul //= 3

if 1 < mul:
    points = 0
print(points)