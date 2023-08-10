import sys
from collections import deque
sys.stdin = open('input.txt')

F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)
visited[S] = 1
que = deque([S])
while que:
    now = que.popleft()
    if now == G:
        print(visited[G]-1)
        break
    if now + U <= F and not visited[now+U]:
        visited[now+U] = visited[now] + 1
        que.append(now+U)
    if now - D > 0 and not visited[now-D]:
        visited[now-D] = visited[now] + 1
        que.append(now-D)
else:
    print('use the stairs')