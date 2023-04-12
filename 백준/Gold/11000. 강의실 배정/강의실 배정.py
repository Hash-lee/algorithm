import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline())


lectures = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)])
classRoom = [lectures[0][1]]
room = 1
for lecture in lectures[1:]:
    if lecture[0] < classRoom[0]:
        heappush(classRoom, lecture[1])
        room += 1
    else:
        heappop(classRoom)
        heappush(classRoom, lecture[1])

print(room)