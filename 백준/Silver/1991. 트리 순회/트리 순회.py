import sys

N = int(sys.stdin.readline())

tree = {}
for _ in range(N):
    mother, left, right = sys.stdin.readline().split()
    tree[mother] = [left, right]


def preorder(alp="A"):
    if alp == ".":
        return ""
    else:
        left, right = tree[alp]
        return alp + preorder(left) + preorder(right)


def inorder(alp="A"):
    if alp == ".":
        return ""
    else:
        left, right = tree[alp]
        return inorder(left) + alp + inorder(right)


def postorder(alp="A"):
    if alp == ".":
        return ""
    else:
        left, right = tree[alp]
        return postorder(left) + postorder(right) + alp


print(preorder())
print(inorder())
print(postorder())