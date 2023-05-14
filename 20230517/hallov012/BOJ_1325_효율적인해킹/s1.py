import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    g[b].append(a)

ans_cnt = 0
ans_lst = []
for i in range(1, n+1):
    visited = [0] * (n+1)
    visited[i] = 1
    cnt = 1
    que = deque([i])
    while que:
        x = que.popleft()
        for y in g[x]:
            if not visited[y]:
                visited[y] = 1
                que.append(y)
                cnt += 1
    if ans_cnt < cnt:
        ans_cnt = cnt
        ans_lst = [i]
    elif ans_cnt <= cnt:
        ans_lst.append(i)

ans_lst.sort()
print(*ans_lst)


