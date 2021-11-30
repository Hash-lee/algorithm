test_num = int(input())

for i in range(test_num):
    k = int(input())
    numbers = list(map(int, input().split()))
    max_sum = -500
    for j in range(len(numbers)-1):
        if numbers[j] + numbers[j+1] > max_sum:
            max_sum = numbers[j] + numbers[j+1]
    print('#{0} {1}'.format(i+1, max_sum))