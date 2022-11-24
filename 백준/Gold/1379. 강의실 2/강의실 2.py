import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
lectures = []
for _ in range(N):
    num, start, end = map(int, sys.stdin.readline().split())
    lectures.append((start, end, num))
numbers = [x[2] for x in lectures]
lectures.sort()


heap = []
room = [0] * (N + 1)
mx = 0
for lecture in lectures:
    s, e, n = lecture
    if not heap:
        mx += 1
        room[n] = 1
        heappush(heap, (e, mx))
    else:
        f, num = heap[0]
        if f <= s:
            heappop(heap)
            heappush(heap, (e, num))
            room[n] = num
        else:
            mx += 1
            heappush(heap, (e, mx))
            room[n] = mx


print(mx)
for number in room[1:]:
    print(number)