본 문제는 모바일 게임 2048을 해보면 쉽게 이해할 수 있는 방식이었습니다.

```python
import sys
sys.stdin = open('s_input.txt', 'r')

# 슬라이드 방향에 따른 함수를 별도로 구성하였습니다.
# 부스트캠프 팀원 분은 Array를 돌리는 방식으로 하셔서 이를 줄였다고 합니다.(!!)
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
# up과 left는 row, column만 바꿔주면 해결할 수 있습니다.

# 역순으로 확인해서 정리하도록 변경하였습니다.
# range(N) → range(N-1, -1, -1), append(0) → insert(0, 0)
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
```

