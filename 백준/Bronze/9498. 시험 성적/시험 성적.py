import sys

result = int(sys.stdin.readline())
if result >= 90:
    grade = "A"
elif result >= 80:
    grade = "B"
elif result >= 70:
    grade = "C"
elif result >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)