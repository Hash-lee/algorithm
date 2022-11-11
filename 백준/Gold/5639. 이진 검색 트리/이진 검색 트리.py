import sys

sys.setrecursionlimit(10**5)

tree = {}

numbers = list(map(int, sys.stdin.readlines()))
root = numbers[0]
stack = []
for idx in range(len(numbers)):
    if stack:
        if numbers[idx] < stack[-1]:
            if not tree.get(stack[-1], 0):
                tree[stack[-1]] = [numbers[idx], 0]
        else:
            while stack[-1] < numbers[idx]:
                last = stack.pop()
                if stack and stack[-1] < numbers[idx]:
                    continue
                else:
                    if tree.get(last, 0):
                        tree[last][1] = numbers[idx]
                    else:
                        tree[last] = [0, numbers[idx]]
                    break
    stack.append(numbers[idx])


def postorder(number):
    if number:
        left, right = tree.get(number, [0, 0])
        postorder(left)
        postorder(right)
        print(number)


postorder(root)
