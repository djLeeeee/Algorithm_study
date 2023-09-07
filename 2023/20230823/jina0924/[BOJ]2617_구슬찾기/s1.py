# 백준 2617번 구슬찾기

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
weight = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    # a > b인 경우만 저장
    weight[a][b] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            # a > k이고 k > b이면 a > k
            if weight[a][k] and weight[k][b]:
                weight[a][b] = 1

ans = 0
for a in range(1, N + 1):
    lc, hc = 0, 0
    for b in range(1, N + 1):
        if a == b:
            continue
        if weight[a][b] == 1:
            hc += 1
        if weight[b][a] == 1:
            lc += 1
    if lc > N // 2 or hc > N // 2:
        ans += 1
print(ans)


