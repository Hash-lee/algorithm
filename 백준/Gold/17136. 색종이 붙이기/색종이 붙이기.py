paper = {0:5, 1:5, 2:5, 3:5, 4:5}

arr = [list(map(int, input().split())) for _ in range(10)]
result = -1

# 색종이 덮기
def cover(r, c, k):
    for i in range(k+1):
        for j in range(k+1):
            arr[r+i][c+j] = 0

# 색종이 빼기
def recover(r, c, k):
    for i in range(k+1):
        for j in range(k+1):
            arr[r+i][c+j] = 1

# 완전 탐색
def sc(s=0):
    global result
    if result != -1 and result <= s: return
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 1:
                for k in range(4, -1, -1):
                    if 0 < paper[k] and r+k < 10 and c+k < 10:
                        if arr[r+k][c] and arr[r][c+k] and arr[r+k][c+k]:
                            x = 1
                            for i in range(k+1):
                                for j in range(k+1):
                                    if arr[r+i][c+j] == 0:
                                        x = 0
                            if x:
                                paper[k] -= 1
                                cover(r, c, k)
                                sc(s+1)
                                paper[k] += 1
                                recover(r, c, k)
                return
    if result == -1 or s < result:
        result = s
sc()
print(result)