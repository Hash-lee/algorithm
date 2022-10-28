import sys

T = sys.stdin.readline()
for tc in range(int(T)):

    lst = list(map(int, sys.stdin.readline().split()))
    N, grades = lst[0], lst[1:]
    avg = sum(grades) / N

    prm = 0
    for grade in grades:
        if grade > avg:
            prm += 1

    ratio = prm / N * 100
    print(f"{ratio:.3f}" + "%")