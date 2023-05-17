import sys
string = sys.stdin.readline().strip()
levels = {0:[]}


def back(string):
    s = []
    idx = 0
    while idx < len(string):
        if string[idx] == "*" or string[idx] == "/":
            s[-1] = (s[-1]+string[idx+1]+string[idx])
            idx += 1
        else:
            s.append(string[idx])
        idx += 1

    t = []
    idx = 0
    while idx < len(s):
        if s[idx] == "+" or s[idx] == "-":
            t.append(s[idx+1]+s[idx])
            idx += 1
        else:
            t.append(s[idx])
        idx += 1
    return "".join(t)

def convert(string):
    level = 0
    idx = 0
    while idx < len(string):
        if string[idx] == "(":
            level += 1
            levels[level] = []
        elif string[idx] == ")":
            levels[level-1].append(back(levels[level]))
            level -= 1
        else:
            levels[level].append(string[idx])
        idx += 1

convert(string)
print(back(levels[0]))