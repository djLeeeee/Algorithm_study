import sys
from collections import deque
sys.stdin = open('input.txt')

a, b, c, d = map(int, input().split())
visited = [[-1] * (b+1) for _ in range(a+1)]
visited[0][0] = 0
que = deque([(0, 0)])

# 같으면 양쪽 채우고 끝
if (a, b) == (c, d):
    print(2)
    exit()
# 그냥 빈거면 끝
if (c, d) == (0, 0):
    print(0)
    exit()

if 1 in (a, b):
    if b > a:
        a, b = b, a
        c, d = d, c
    if c == 1:
        print(2*(b-d))
    else:
        print(2*(b-d)+1)
    exit()


while que:
    x, y = que.popleft()
    if (x, y) == (c, d):
        break

    # A 물통을 채우기, 비우기
    if visited[a][y] == -1:
        visited[a][y] = visited[x][y] + 1
        que.append((a, y))
    if visited[0][y] == -1:
        visited[0][y] = visited[x][y] + 1
        que.append((0, y))
    # B 물통 채우기, 비우기
    if visited[x][b] == -1:
        visited[x][b] = visited[x][y] + 1
        que.append((x, b))
    if visited[x][0] == -1:
        visited[x][0] = visited[x][y] + 1
        que.append((x, 0))
    # A => B, B => A 옮기기
    if x <= b-y:
        if visited[0][y+x] == -1:
            visited[0][y+x] = visited[x][y] + 1
            que.append((0, y+x))
    else:
        if visited[x-(b-y)][b] == -1:
            visited[x-(b-y)][b] = visited[x][y] + 1
            que.append((x-(b-y), b))
    if y <= a-x:
        if visited[x+y][0] == -1:
            visited[x+y][0] = visited[x][y] + 1
            que.append((x+y, 0))
    else:
        if visited[a][y-(a-x)] == -1:
            visited[a][y-(a-x)] = visited[x][y] + 1
            que.append((a, y-(a-x)))


print(visited[c][d])



