# 백준 20056번 마법사 상어와 파이어볼

import sys
sys.stdin = open('input5.txt')
from collections import deque

dr, dc = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)

N, M, K = map(int, input().split())                 # N: 격자의 크기, M: 파이어볼 개수, K: 명령 횟수
fireball = deque([])
for _ in range(M):
    fireball.append(list(map(int, input().split())) + [1])
while K:
    ball2 = {}
    while fireball:
        r, c, m, s, d, cnt = fireball.popleft()
        nr, nc = (r + dr[d] * s) % N, (c + dc[d] * s) % N
        if ball2.get((nr, nc)):
            ball2.get((nr, nc))[0] += m
            ball2.get((nr, nc))[1] += s
            ball2.get((nr, nc))[3] += 1
            if ball2.get((nr, nc))[2] >= 10 or ball2.get((nr, nc))[2] % 2 != d % 2:
                ball2.get((nr, nc))[2] = 10
            else:
                if d % 2:
                    ball2.get((nr, nc))[2] = 1
                else:
                    ball2.get((nr, nc))[2] = 0
        else:
            ball2[(nr, nc)] = [m, s, d, cnt]
    print('new')
    for key, value in ball2.items():
        print(value)
        r, c = key
        m, s, d, cnt = value
        if cnt > 1:
            if d > 1 and m // 5:
                for i in range(1, 8, 2):
                    fireball.append([r, c, m//5, s//cnt, i, 1])
            elif d <= 1 and m // 5:
                for j in range(0, 7, 2):
                    fireball.append([r, c, m//5, s//cnt, j, 1])
        elif cnt == 1 and m:
            fireball.append([r, c, m, s, d, cnt])
    print(fireball)
    K -= 1
ans = 0
for ball in fireball:
    ans += ball[2]
print(ans)