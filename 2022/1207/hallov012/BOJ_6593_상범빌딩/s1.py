import sys
from collections import deque
sys.stdin = open('input.txt')

df = [0, 0, 0, 0, 1, -1]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]

input = sys.stdin.readline

while True:
    l, r, c = map(int, input().split())
    if (l, r, c) == (0, 0, 0):
        break
    arr = []
    sf, sx, sy = 0, 0, 0
    ef, ex, ey = 0, 0, 0
    for i in range(l):
        floor = []
        for j in range(r):
            line = list(input().rstrip())
            floor.append(line)
            for k in range(c):
                if line[k] == 'S':
                    sf, sx, sy = i, j, k
                elif line[k] == 'E':
                    ef, ex, ey = i, j, k
        arr.append(floor)
        input()
    arr[sf][sx][sy] = 0
    que = deque([(sf, sx, sy)])
    ans = -1
    while que:
        f, x, y = que.popleft()
        if (f, x, y) == (ef, ex, ey):
            ans = arr[f][x][y]
            break
        for i in range(6):
            nf = f + df[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nf < l and 0 <= nx < r and 0 <= ny < c:
                if arr[nf][nx][ny] == '.' or arr[nf][nx][ny] == 'E':
                    arr[nf][nx][ny] = arr[f][x][y] + 1
                    que.append((nf, nx, ny))
    if ans == -1:
        print('Trapped!')
    else:
        print(f"Escaped in {ans} minute(s).")
