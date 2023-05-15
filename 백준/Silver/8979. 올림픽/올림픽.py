num, what_rank = map(int, input().split())

nations = []
for i in range(num):
    nations.append(list(map(int, input().split())))
for nation in nations:
    tmp = nation.pop(0)
    nation.append(tmp)

nations.sort()
nations.reverse()

for i in range(len(nations)):
    if i == 0:
        nations[i].append(i+1)
    elif nations[i][0] == nations[i-1][0] and nations[i][1] == nations[i-1][1] and nations[i][2] == nations[i-1][2]:
        nations[i].append(nations[i - 1][-1])
    else:
        nations[i].append(i+1)

for nation in nations:
    if nation[-2] == what_rank:
        print(nation[-1])