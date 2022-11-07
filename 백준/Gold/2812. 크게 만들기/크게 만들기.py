import sys

N, K = map(int, sys.stdin.readline().split())
numbers = sys.stdin.readline().rstrip()


stack = []
for number in numbers:
    if not stack:
        stack.append(number)
    else:
        while stack and stack[-1] < number and K:
            stack.pop()
            K -= 1
        stack.append(number)
while K:
    stack.pop()
    K -= 1


print("".join(stack))