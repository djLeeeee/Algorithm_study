import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(idx):
    if idx == n:
        for i in range(1, 10):
            for j in range(1, 10):
                print(arr[i][j], end='')
            print()
        exit()
    x, y = empty[idx]
    a, b = (x-1)//3, (y-1)//3
    s_idx = a * 3 + b + 1
    possible = check_num(x, y, s_idx)
    for num in possible:
        row[x][num] = col[y][num] = square[s_idx][num] = 1
        arr[x][y] = num
        find(idx+1)
        row[x][num] = col[y][num] = square[s_idx][num] = 0
        arr[x][y] = 0

def check_num(x, y, s_idx):
    tmp = []
    for i in range(1, 10):

        if not row[x][i] and not col[y][i] and not square[s_idx][i]:
            tmp.append(i)
    return tmp


empty = []
arr = [[0] * 10]
row = [[0] * 10 for _ in range(10)]
col = [[0] * 10 for _ in range(10)]
square = [[0] * 10 for _ in range(10)]

for i in range(1, 10):
    line = input()
    line_lst = [0]
    for j in range(1, 10):
        val = int(line[j-1])
        line_lst.append(val)
        if val:
            row[i][val] = 1
            col[j][val] = 1
            x, y = (i-1)//3, (j-1)//3
            idx = x * 3 + y + 1
            square[idx][val] = 1
        else:
            empty.append((i, j))
    arr.append(line_lst)

n = len(empty)
find(0)




