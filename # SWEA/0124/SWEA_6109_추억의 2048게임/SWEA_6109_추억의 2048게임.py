import sys
sys.stdin = open('s_input.txt', 'r')

def move_up():
    for c in range(N):
        tmp_list = [0] * N
        idx = -1
        for r in range(N):
            if arr[r][c]:
                idx += 1
                tmp_list[idx] = arr[r][c]
        for i in range(N-1):
            if tmp_list[i] == 0: break
            if tmp_list[i] == tmp_list[i+1]:
                tmp_list[i] = tmp_list[i]*2
                tmp_list.pop(i+1)
                tmp_list.append(0)
        for j in range(N):
            arr[j][c] = tmp_list[j]

def move_down():
    for c in range(N):
        tmp_list = [0] * N
        idx = 0
        for r in range(N-1, -1, -1):
            if arr[r][c]:
                idx -= 1
                tmp_list[idx] = arr[r][c]
        for i in range(N-1, -1, -1):
            if tmp_list[i] == 0: break
            if tmp_list[i] == tmp_list[i-1]:
                tmp_list[i] = tmp_list[i]*2
                tmp_list.pop(i-1)
                tmp_list.insert(0, 0)
        for j in range(N):
            arr[j][c] = tmp_list[j]

def move_left():
    for r in range(N):
        tmp_list = [0] * N
        idx = -1
        for c in range(N):
            if arr[r][c]:
                idx += 1
                tmp_list[idx] = arr[r][c]
        for i in range(N-1):
            if tmp_list[i] == 0: break
            if tmp_list[i] == tmp_list[i+1]:
                tmp_list[i] = tmp_list[i]*2
                tmp_list.pop(i+1)
                tmp_list.append(0)
        for j in range(N):
            arr[r][j] = tmp_list[j]

def move_right():
    for r in range(N):
        tmp_list = [0] * N
        idx = 0
        for c in range(N-1, -1, -1):
            if arr[r][c]:
                idx -= 1
                tmp_list[idx] = arr[r][c]
        for i in range(N-1, -1, -1):
            if tmp_list[i] == 0: break
            if tmp_list[i] == tmp_list[i-1]:
                tmp_list[i] = tmp_list[i]*2
                tmp_list.pop(i-1)
                tmp_list.insert(0, 0)
        for j in range(N):
            arr[r][j] = tmp_list[j]

for tc in range(1, int(input())+1):
    N, dir = input().split()
    N = int(N)
    arr = [list(map(int, input().split())) for _ in range(N)]

    if dir == 'up':
        move_up()
    elif dir == 'down':
        move_down()
    elif dir == 'left':
        move_left()
    elif dir == 'right':
        move_right()
    
    print(f'#{tc}')
    for a in arr:
        str_a = list(map(str, a))
        print(" ".join(str_a))