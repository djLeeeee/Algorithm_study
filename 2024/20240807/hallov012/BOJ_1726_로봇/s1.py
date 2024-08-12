import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

def get_dir(d):
    if d == 1:
        return 2
    elif d == 2:
        return 1
    return d

def get_fast(a, b):
    val1 = (a-b) % 4
    val2 = (b-a) % 4
    return min(val1, val2)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
x1, y1, d1 = (val - 1 for val in map(int, input().split()))
x2, y2, d2 = (val - 1 for val in map(int, input().split()))
d1, d2 = get_dir(d1), get_dir(d2)

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[[sys.maxsize] * 4 for _ in range(m)] for _ in range(n)]
visited[x1][y1][d1] = 0
que = deque([(x1, y1, d1, 0)])

ans = sys.maxsize
while que:
    x, y, d, v = que.popleft()
    if x == x2 and y == y2:
        ans = min(ans, v + get_fast(d, d2))
        continue
    if visited[x][y][d] < v:
        continue

    for i in range(4):
        val = v + 1 + get_fast(d, i)
        nx, ny = x, y
        for _ in range(3):
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
                if visited[nx][ny][i] > val:
                    visited[nx][ny][i] = val
                    que.append((nx, ny, i, val))
            else:
                break

print(ans)

