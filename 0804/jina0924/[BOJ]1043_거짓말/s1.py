# 백준 1043번 거짓말 -3% x

import sys
sys.stdin = open('input8.txt')
input = sys.stdin.readline


# def union(x, y):
#     p[find_set(y)] = find_set(x)
#
#
# def find_set(x):
#     if p[x] != x:
#         p[x] = find_set(p[x])
#     return p[x]


N, M = map(int, input().split())
knower_cnt, *already = map(int, input().split())
already = set(already)
data = []
for _ in range(M):
    cnt, *party = map(int, input().split())
    for i in range(cnt):
        if party[i] in already:
            already = already | set(party)
            break
    data.append(party)
ans = 0
for i in range(M):
    if not set(data[i]) & already:
        ans += 1
print(ans)