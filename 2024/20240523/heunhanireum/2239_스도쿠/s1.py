import sys
sys.stdin = open('input.txt')

sdk = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]
zero = []

def is_valid(r, c, num):
    sr, sc = (r//3)*3, (c//3)*3
    for nr in range(3):
        for nc in range(3):
            if sdk[sr+nr][sc+nc] == num:
                return False

    for i in range(9):
        if sdk[i][c] == num or sdk[r][i] == num:
            return False

    return True

for r in range(9):
    for c in range(9):
        if sdk[r][c] == 0:
            zero.append((r, c))


def sudoku(idx):
    if idx >= len(zero):
        for rr in sdk:
            print(''.join(map(str, rr)))
        exit()
    r, c = zero[idx][0], zero[idx][1]
    for i in range(1, 10):
        if is_valid(r, c, i):
            sdk[r][c] = i
            sudoku(idx+1)
            sdk[r][c] = 0

sudoku(0)