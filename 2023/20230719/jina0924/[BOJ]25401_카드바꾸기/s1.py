# 백준 25401번 카드 바꾸기

import sys
sys.stdin = open('input.txt')
from itertools import combinations as C

N = int(input())
cards = list(map(int, input().split()))
ans = N - 2
tmp = set()

# 공차랑 첫항 구하기
for i, j in C(range(N), 2):
    d = (cards[i] - cards[j]) / (i - j)
    if d == int(d):
        tmp.add((cards[i] - d * i, d))

# 등차수열 아닌 항의 개수 세기
for s, d in tmp:
    cnt = 0
    for k in range(N):
        if cards[k] != s + d * k:
            cnt += 1
    ans = min(ans, cnt)
print(ans)
