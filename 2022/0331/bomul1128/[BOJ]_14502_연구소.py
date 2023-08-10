from sys import stdin
from copy import deepcopy

input = stdin.readline


def sol(x1, y1, x2, y2, x3, y3):
    lab = deepcopy(board)
    lab[x1][y1] = 1
    lab[x2][y2] = 1
    lab[x3][y3] = 1
    starts = deepcopy(virus)
    result = l - 3
    while starts:
        x, y = starts.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                result -= 1
                starts.append((nx, ny))
        if result <= ans:
            return result
    return result


n, m = map(int, input().split())
board = []
empty = []
virus = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 0:
            empty.append((i, j))
        elif line[j] == 2:
            virus.append((i, j))
    board.append(line)
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
l = len(empty)
for i in range(l - 2):
    for j in range(i + 1, l - 1):
        for k in range(j + 1, l):
            ans = max(ans, sol(*empty[i], *empty[j], *empty[k]))
print(ans)
