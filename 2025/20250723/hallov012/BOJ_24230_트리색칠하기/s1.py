import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
color = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

que = deque()
que.append(1)
visited = [0] * (n+1)
visited[1] = 1
ans = 1 if color[1] else 0
while que:
    x = que.popleft()
    for y in tree[x]:
        if not visited[y]:
            visited[y] = 1
            que.append(y)
            if color[x] != color[y]:
                ans += 1

print(ans)
