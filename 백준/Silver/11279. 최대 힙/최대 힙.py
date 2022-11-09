import sys

N = int(sys.stdin.readline())

heap = [0] * N
idx = -1
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        idx += 1
        heap[idx] = x
        lower = idx
        upper = idx
        while 0 < upper:
            if upper % 2:
                upper = (upper - 1) // 2
            else:
                upper = (upper - 2) // 2
            if heap[upper] < heap[lower]:
                heap[upper], heap[lower] = heap[lower], heap[upper]
            else:
                break
            lower = upper
    else:
        print(heap[0])
        if heap[0]:
            heap[0], heap[idx] = heap[idx], 0
            idx -= 1

            upper = 0
            while True:
                left = upper * 2 + 1
                right = upper * 2 + 2
                if idx < left:
                    break
                lower = left
                if right <= idx and heap[left] < heap[right]:
                    lower = right
                if heap[upper] < heap[lower]:
                    heap[upper], heap[lower] = heap[lower], heap[upper]
                    upper = lower
                else:
                    break