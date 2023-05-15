alp = []
f = int(input())
for i in range(f):
    name = input()
    alp.append(name[0])

first = sorted(list(set(alp)))
result = ''

for j in first:
    if alp.count(j) >= 5:
        result += j

if result == '':
    result = 'PREDAJA'
print(result)