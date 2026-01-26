import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, k, m = map(int, input().split())
stations = [[] for _ in range(n)]
tubes = []

for t_idx in range(m):
    s_lst = [x-1 for x in list(map(int, input().split()))]
    tubes.append(s_lst)
    for s in s_lst:
        stations[s].append(t_idx)

if n == 1:
    print(1)
    exit()

visited_station = [0] * n
visited_tube = [0] * m
visited_station[0] = 1

que = deque([(0, 1)])
ans = -1
while que:
    now, cnt = que.popleft()
    if now == n-1:
        ans = cnt
        break
    for t_idx in stations[now]:
        if not visited_tube[t_idx]:
            visited_tube[t_idx] = 1
            for s_idx in tubes[t_idx]:
                if not visited_station[s_idx]:
                    visited_station[s_idx] = 1
                    que.append((s_idx, cnt+1))
print(ans)