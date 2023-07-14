from collections import deque
import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread():
    for x, y, amount in dusts:
        cnt = 0
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if (0 <= nx < R and 0 <= ny < C) and new_arr[nx][ny] != -1:
                new_arr[nx][ny] += int(amount/5)
                cnt += 1
        new_arr[x][y] += (amount - int(amount/5)*cnt)

def clean():
    # 우 상 좌 하
    dx1 = [0, -1, 0, 1]
    dy1 = [1, 0, -1, 0]
    x, y = cleaners[0]
    remember1 = deque([0])
    flag1 = 1
    i = 0
    while flag1:
        nx = x + dx1[i]
        ny = y + dy1[i]
        if 0 <= nx < R and 0 <= ny < C and new_arr[nx][ny] == -1:
            flag1 = 0
        elif 0 <= nx < R and 0 <= ny < C:
            remember1.append(new_arr[nx][ny])
            new_arr[nx][ny] = remember1.popleft()
            x, y = nx, ny
        else:
            i += 1
    # 우 하 좌 상
    dx2 = [0, 1, 0, -1]
    dy2 = [1, 0, -1, 0]
    x, y = cleaners[1]
    remember2 = deque([0])
    flag2 = 1
    i = 0
    while flag2:
        nx = x + dx2[i]
        ny = y + dy2[i]
        if 0 <= nx < R and 0 <= ny < C and new_arr[nx][ny] == -1:
            flag2 = 0
        elif 0 <= nx < R and 0 <= ny < C:
            remember2.append(new_arr[nx][ny])
            new_arr[nx][ny] = remember2.popleft()
            x, y = nx, ny
        else:
            i += 1


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
for i in range(T):
    dusts = []
    cleaners = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] and arr[i][j] != -1:
                dusts.append((i, j, arr[i][j]))
            elif arr[i][j] == -1:
                cleaners.append((i, j))
    new_arr = [[0]*C for __ in range(R)]
    for x, y in cleaners:
        new_arr[x][y] = -1
    spread()
    clean()
    arr = new_arr
result = 0
for idx1 in range(R):
    for idx2 in range(C):
        if arr[idx1][idx2] != -1:
            result += arr[idx1][idx2]
print(result)