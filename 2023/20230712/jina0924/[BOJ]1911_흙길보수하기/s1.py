# 1911번 흙길 보수하기

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, L = map(int, input().split())        # 웅덩이 개수, 널빤지 길이
puddles = [list(map(int, input().split())) for _ in range(N)]
puddles.sort(key=lambda x: x[0])        # 웅덩이 시작점을 기준으로 정렬
ans = 0
p = puddles[0][0]                       # 현재 살펴볼 널빤지 시작점
for s, e in puddles:
    if s < p:                           # 웅덩이 시작점 이후까지 널빤지 놓인 상황
        l = e - p
    else:
        l = e - s
        p = s
    cnt = l // L                        # 웅덩이 길이만큼 널빤지 놓기
    if l % L:
        cnt += 1
    ans += cnt
    p += cnt * L
print(ans)