def solution(s):
    def precheck(string):
        left = [0, 0, 0]
        right = [0, 0, 0]
        for p in string:
            if p == ")": right[0] += 1
            if p == "]": right[1] += 1
            if p == "}": right[2] += 1
            if p == "(": left[0] += 1
            if p == "[": left[1] += 1
            if p == "{": left[2] += 1
        for idx in range(3):
            l, r = left[idx], right[idx]
            if l != r: return True
        return False
    if precheck(s): return 0

    def check(string):
        stack = []
        for p in string:
            if p == "]" or p == "}" or p == ")":
                if stack:
                    c = stack.pop()
                    if (c == "[" and p == "]") or (c == "{" and p == "}") or (c == "(" and p == ")"):
                        continue
                return False
            else:
                stack.append(p)
        return True
    answer = 0
    
    for idx in range(len(s) - 1):
        if check(s[idx:] + s[:idx]):
            answer += 1
    return answer