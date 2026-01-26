import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k, m, p = map(int, input().split())
    g = [[] for _ in range(m+1)]
    in_cnt = [0] * (m+1)
    for _ in range(p):
        a, b = map(int, input().split())
        g[a].append(b)
        in_cnt[b] += 1
    que = deque()
    strahler = [[] for _ in range(m+1)]
    for i in range(1, m+1):
        if not in_cnt[i]:
            que.append(i)
            strahler[i] = [1, 0]

    while que:
        x = que.popleft()
        order = sum(strahler[x])
        for nx in g[x]:
            in_cnt[nx] -= 1
            # 새로운 순서로 갱신
            if not strahler[nx] or strahler[nx][0] < order:
                strahler[nx] = [order, 0]
            # order + 1 되어야하니까 Flag 갱신
            elif strahler[nx][0] == order:
                strahler[nx][1] = 1
            if not in_cnt[nx]:
                que.append(nx)
    print(k, sum(strahler[m]))

