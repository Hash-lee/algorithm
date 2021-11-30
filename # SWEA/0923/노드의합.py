import sys
sys.stdin = open('노드의합.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M, L = map(int, input().split())
    nodes = [0] * (N + 1)
    for _ in range(M):
        l, n = map(int, input().split())
        nodes[l] += n
        while l >= 2:
            nodes[l//2] += n
            l = l//2
    print('#{} {}'.format(t, nodes[L]))