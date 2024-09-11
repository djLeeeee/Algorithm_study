import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def rotate(dir):
    # 오
    if dir == 0:
        dice[4], dice[1], dice[3], dice[6] = dice[6], dice[4], dice[1], dice[3]
    # 왼
    elif dir == 1:
        dice[4], dice[1], dice[3], dice[6] = dice[1], dice[3], dice[6], dice[4]
    # 위
    elif dir == 2:
        dice[2], dice[1], dice[5], dice[6] = dice[1], dice[5], dice[6], dice[2]
    # 아래
    elif dir == 3:
        dice[2], dice[1], dice[5], dice[6] = dice[6], dice[2], dice[1], dice[5]

n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
orders = [i-1 for i in(list(map(int, input().split())))]
# 오, 왼, 위, 아래
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
top, bottom = 1, 6

dice = [0] * 7
dice[bottom] = arr[x][y]
for dir in orders:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny
        rotate(dir)
        print(dice[top])
        if arr[x][y]:
            dice[bottom] = arr[x][y]
            arr[x][y] = 0
        else:
            arr[x][y] = dice[bottom]



