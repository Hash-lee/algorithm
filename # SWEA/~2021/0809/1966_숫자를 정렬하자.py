T = int(input())

for i in range(T):
    k = int(input())
    numbers = list(map(int, input().split()))  
    for l in range(k):
        for j in range(k-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    print('#{0} {1}'.format(i+1, " ".join(map(str, numbers))))