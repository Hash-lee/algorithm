import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
mx = -1

# case1
# B B H
full = sum(numbers) * 2
temp1 = full - numbers[0] * 3
for idx in range(1, N - 1):
    temp1 += numbers[idx - 1]
    temp1 -= numbers[idx] * 2
    mx = temp1 if mx < temp1 else mx

# case2
# H B B
temp2 = full - numbers[-1] * 3
for idx in range(-2, -N - 1, -1):
    temp2 += numbers[idx + 1]
    temp2 -= numbers[idx] * 2
    mx = temp2 if mx < temp2 else mx

# case3
# B H B
temp3 = sum(numbers) - numbers[0] - numbers[-1]
for idx in range(1, N - 1):
    mx = temp3 + numbers[idx] if mx < temp3 + numbers[idx] else mx

print(mx)
