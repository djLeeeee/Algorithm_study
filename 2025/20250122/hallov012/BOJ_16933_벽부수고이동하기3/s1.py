import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 0: 밤, 1: 낮
visited = [[[0 for _ in range(m)]for _ in range(n)]for _ in range(k+1)]
visited[0][0][0] = 1
que = deque()
# x, y, 벽 부순 횟수, 이동 횟수
que.append((0, 0, 0, 0))

# 제자리에 머무는건 앞에 벽이 있을 때만 고려하면?
while que:
    x, y, cnt, day = que.popleft()
    if x == n-1 and y == m-1:
        print(day+1)
        break

    t = (day+1) % 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            # 이동 가능
            if arr[nx][ny] == '0':
                if not visited[cnt][nx][ny]:
                    visited[cnt][nx][ny] = 1
                    que.append((nx, ny, cnt, day+1))
            # 벽을 부술 수 있다면 부숨
            elif cnt < k and arr[nx][ny] == '1' and not visited[cnt+1][nx][ny]:
                if not t:
                    que.append((x, y, cnt, day+1))
                else:
                    visited[cnt+1][nx][ny] = 1
                    que.append((nx, ny, cnt+1, day+1))
else:
    print(-1)

