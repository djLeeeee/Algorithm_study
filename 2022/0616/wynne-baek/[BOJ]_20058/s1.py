import sys
from collections import deque
sys.stdin = open('input.txt')

def rotate_and_melt(L, arr):
    new_arr = [[0] * len_of_arr for _ in range(len_of_arr)]
    small_size = 2 ** L
    for i in range(0, len_of_arr, small_size):
        for j in range(0, len_of_arr, small_size):
            for x in range(small_size):
                for y in range(small_size):
                    new_arr[i + x][j + y] = arr[i + small_size - y - 1][j + x]
    arr = new_arr
    melt_list = []
    for x in range(len_of_arr):
        for y in range(len_of_arr):
            ice_cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len_of_arr and 0 <= ny < len_of_arr and arr[nx][ny] > 0:
                    ice_cnt += 1
            if ice_cnt < 3 and arr[x][y]:
                melt_list.append((x, y))
    for x, y in melt_list:
        arr[x][y] -= 1
    return arr

def check_ice(arr):
    global len_of_arr
    visited = [[0] * len_of_arr for _ in range(len_of_arr)]
    max_area_cnt = 0
    for x in range(len_of_arr):
        for y in range(len_of_arr):
            area_cnt = 0
            if visited[x][y] or arr[x][y] == 0:
                continue
            queue = deque([(x, y)])
            visited[x][y] = 1

            while queue:
                x, y = queue.popleft()
                area_cnt += 1

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < len_of_arr and 0 <= ny < len_of_arr and not visited[nx][ny] and arr[nx][ny] != 0:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
            max_area_cnt = max(max_area_cnt, area_cnt)
    print(max_area_cnt)

N, Q = map(int, input().split())
len_of_arr = 2 ** N
arr = [list(map(int, input().split())) for _ in range(len_of_arr)]
# print(arr)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

attacks = list(map(int, input().split()))
for i in attacks:
    arr = rotate_and_melt(i, arr)
# print(arr)
ans1 = sum(sum(s) for s in arr)
print(ans1)
check_ice(arr)


