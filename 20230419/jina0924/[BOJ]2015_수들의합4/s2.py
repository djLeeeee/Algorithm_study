# 백준 2015번 수들의 합 4

import sys
sys.stdin = open('input.txt')
from collections import defaultdict

N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = defaultdict(int)
ans = 0
cnt[0] = 1                          # 아무것도 더하지 않은 상태의 누적값 경우의 수 1 올려줌
total = 0
for num in arr:
    total += num                    # 현재 위치까지의 누적합을 담는 변수
    if cnt[total - K]:              # total - (total - K) = K이므로
        ans += cnt[total - K]       # 누적합이 (total - K)였던 경우의 수만큼 K를 만들 수 있음
    cnt[total] += 1                 # 현재 구한 누적합 개수 1 올려줌
print(ans)