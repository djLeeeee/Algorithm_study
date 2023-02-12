import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[sys.maxsize] * 10 for _ in range(10)]
g = [0] * 100
for _ in range(n+m):
    a, b = map(int, input().split())
    g[a-1] = b-1
visited[0][0] = 0
que = deque([(0, 0)])
while que:
    now, cnt = que.popleft()
    for i in range(1, 7):
        next = now+i
        if next < 100:
            if g[next]:
                next = g[next]
            nx = next // 10
            ny = next % 10
            if cnt + 1 < visited[nx][ny]:
                visited[nx][ny] = cnt+1
                que.append((next, cnt+1))
print(visited[-1][-1])