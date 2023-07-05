import sys
sys.stdin = open('input.txt')


def symmetry(idx, cnt):
    x, y = len(arr), len(arr[0])
    cnt %= 2
    if cnt:
        # 1번
        if idx == 1:
            for j in range(y):
                for i in range(x//2):
                    arr[i][j], arr[x-i-1][j] = arr[x-i-1][j], arr[i][j]

        # 2번
        elif idx == 2:
            for i in range(x):
                for j in range(y//2):
                    arr[i][j], arr[i][y-j-1] = arr[i][y-j-1], arr[i][j]

def rotate(cnt):
    cnt %= 4
    x, y = len(arr), len(arr[0])
    # 홀수 => 행과 열이 뒤바뀜
    if cnt % 2:
        temp = [[0] * x for _ in range(y)]
    else:
        temp = [[0] * y for _ in range(x)]

    if not cnt:
        return arr

    elif cnt == 1:
        for i in range(x):
            for j in range(y):
                temp[j][x-i-1] = arr[i][j]

    elif cnt == 2:
        for i in range(x):
            for j in range(y):
                temp[x-i-1][y-j-1] = arr[i][j]

    elif cnt == 3:
        for i in range(x):
            for j in range(y):
                temp[y-j-1][i] = arr[i][j]

    return temp

def change(cnt):
    x, y = len(arr), len(arr[0])
    half_x, half_y = x//2, y//2
    cnt %= 4
    temp = [[0] * y for _ in range(x)]

    if not cnt:
        return arr

    elif cnt == 1:
        for i in range(x):
            if i < half_x:
                for j in range(y):
                    if j < half_y:
                        temp[i][half_y + j] = arr[i][j]
                    else:
                        temp[half_x + i][j] = arr[i][j]
            else:
                for j in range(y):
                    if j < half_y:
                        temp[i - half_x][j] = arr[i][j]
                    else:
                        temp[i][j - half_y] = arr[i][j]
    elif cnt == 2:
        for i in range(x):
            if i < half_x:
                for j in range(y):
                    if j < half_y:
                        temp[half_x + i][half_y + j] = arr[i][j]
                    else:
                        temp[half_x + i][j - half_y] = arr[i][j]
            else:
                for j in range(y):
                    if j < half_y:
                        temp[i - half_x][half_y + j] = arr[i][j]
                    else:
                        temp[i - half_x][j - half_y] = arr[i][j]
    elif cnt == 3:
        for i in range(x):
            if i < half_x:
                for j in range(y):
                    if j < half_y:
                        temp[half_x + i][j] = arr[i][j]
                    else:
                        temp[i][j - half_y] = arr[i][j]
            else:
                for j in range(y):
                    if j < half_y:
                        temp[i][half_y + j] = arr[i][j]
                    else:
                        temp[i - half_x][j] = arr[i][j]
    return temp

input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))
order_num = {
    1: ('symmetry_vertical', 1),
    2: ('symmetry_horizontal', 1),
    3: ('rotate', 1),
    4: ('rotate', -1),
    5: ('change', 1),
    6: ('change', -1)
}

before = ''
cnt = 0

for i in range(r):
    order, temp_cnt = order_num[orders[i]]
    if order == before:
        cnt += temp_cnt
    if order != before:
        if before == 'symmetry_vertical':
            symmetry(1, cnt)
        elif before == 'symmetry_horizontal':
            symmetry(2, cnt)
        elif before == 'rotate':
            arr = rotate(cnt)
        else:
            arr = change(cnt)
        before = order
        cnt = temp_cnt

if before == 'symmetry_vertical':
    symmetry(1, cnt)
elif before == 'symmetry_horizontal':
    symmetry(2, cnt)
elif before == 'rotate':
    arr = rotate(cnt)
else:
    arr = change(cnt)

for line in arr:
    print(*line)