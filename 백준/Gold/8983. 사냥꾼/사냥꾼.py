import sys

M, N, L = map(int, sys.stdin.readline().split())
shooters = sorted(list(map(int, sys.stdin.readline().split())))
animals = sorted([tuple(map(int, n.split())) for n in sys.stdin.readlines()], key=lambda x: (x[0] + x[1], x[0]))


count = 0
shooter = 0
animal = 0
while shooter < M and animal < N:
    if abs(shooters[shooter] - animals[animal][0]) + animals[animal][1] <= L:
        count += 1
        animal += 1
    else:
        if shooters[shooter] < animals[animal][0]:
            shooter += 1
        else:
            animal += 1

print(count)