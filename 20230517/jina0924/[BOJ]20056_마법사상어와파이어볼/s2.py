# 백준 20056번 마법사 상어와 파이어볼

import sys
sys.stdin = open('input5.txt')
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
dr, dc = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
queue = deque([])
for _ in range(M):
    queue.append(list(map(int, input().split())) + [1])
for _ in range(K):
    position = {}
    while queue:
        r, c, m, s, d, cnt = queue.popleft()
        nr, nc = (r + dr[d] * s) % N, (c + dc[d] * s) % N
        if position.get((nr, nc)):
            position[(nr, nc)][0] += m
            position[(nr, nc)][1] += s
            position[(nr, nc)][3] += 1
            if position[(nr, nc)][2] != 10 and position[(nr, nc)][2] % 2 == d % 2:
                if d % 2:
                    position[(nr, nc)][2] = 1
                else:
                    position[(nr, nc)][2] = 2
            else:
                position[(nr, nc)][2] = 10
        else:
            position[(nr, nc)] = [m, s, d, cnt]
    for key, value in position.items():
        m, s, d, cnt = value
        if cnt >= 2:
            m //= 5
            if m <= 0:
                continue
            s //= cnt
            if d == 10:
                start = 1
            else:
                start = 0
            for nd in range(start, 8, 2):
                queue.append([*key, m, s, nd, 1])
        else:
            queue.append([*key, *value])
ans = 0
for fireball in queue:
    ans += fireball[2]
print(ans)