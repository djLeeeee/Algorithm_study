import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, r1, r2 = map(int, input().split())
g = defaultdict(list)
for _ in range(n-1):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

# r1과 r2 사이의 최단 경로에서 중간에 제일 긴 거리를 빼기
visited = [0] * (n+1)
que = deque([(r1, 0, 0)])
visited[r1] = 1
while que:
    x, cnt, max_d = que.popleft()
    if x == r2:
        print(cnt - max_d)
        break
    for y, d in g[x]:
        if not visited[y]:
            visited[y] = 1
            que.append((y, cnt+d, max(max_d, d)))

