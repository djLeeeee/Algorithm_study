import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def calc(line):
    new_line = []
    cnt = defaultdict(int)
    for num in line:
        if num:
            cnt[num] += 1
    for a, b in sorted(cnt.items(), key=lambda x:(x[1], x[0])):
        new_line.append(a)
        new_line.append(b)
    if len(new_line) > 100:
        new_line = new_line[:100]
    return new_line

def r_operation(arr):
    # 행 -> 열로 변환
    new_arr = []
    max_len = 0
    for row in arr:
        new_row = calc(row)
        new_arr.append(new_row)
        max_len = max(max_len, len(new_row))
    for row in new_arr:
        row.extend([0] * (max_len - len(row)))
    return new_arr


def c_operation(arr):
    # 열 -> 행으로 변환
    transposed = list(zip(*arr))
    new_transposed = []
    max_len = 0
    for col in transposed:
        new_col = calc(col)
        new_transposed.append(new_col)
        max_len = max(max_len, len(new_col))
    for col in new_transposed:
        col.extend([0] * (max_len - len(col)))
    return list(map(list, zip(*new_transposed)))


r, c, k = map(int, input().split())
r -= 1
c -= 1
arr = [list(map(int, input().split())) for _ in range(3)]
for t in range(101):
    row_len, col_len = len(arr), len(arr[0])
    if r < row_len and c < col_len and arr[r][c] == k:
        break
    if row_len >= col_len:
        arr = r_operation(arr)
    else:
        arr = c_operation(arr)
else:
    t = -1

print(t)