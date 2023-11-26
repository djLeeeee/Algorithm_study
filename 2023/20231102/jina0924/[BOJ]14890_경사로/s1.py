# 백준 14890번 경사로

import sys
sys.stdin = open('input.txt')


def can_go(r, c):
    h = data[r][c]
    if h < data[r][c - 1]:
        if c + l > n:
            return False
        for nc in range(c, c + l):
            if data[r][nc] != h or slope[r][nc]:
                return False
            slope[r][nc] = 1
    else:
        h = data[r][c - 1]
        if c - l < 0:
            return False
        for nc in range(c - l, c):
            if data[r][nc] != h or slope[r][nc]:
                return False
            slope[r][nc] = 1
    return True



def road(r):
    x = data[r][0]
    for c in range(1, n):
        if abs(x - data[r][c]) > 1:
            return 0
        if x == data[r][c]:
            continue
        if can_go(r, c):
            x = data[r][c]
        else:
            return 0
    return 1


n, l = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
slope = [[0] * n for _ in range(n)]

ans = 0
for r in range(n):
    ans += road(r)

data = list(map(list, zip(*data)))
slope = [[0] * n for _ in range(n)]
for r in range(n):
    ans += road(r)
print(ans)