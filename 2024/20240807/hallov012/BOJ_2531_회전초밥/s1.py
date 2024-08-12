import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
cnt = defaultdict(int)
plates = [int(input()) for _ in range(n)]
cnt[c] += 1
for i in range(k):
    cnt[plates[i]] += 1

ans = len(cnt.keys())
l, r = 0, k
while l < n:
    l_value, r_value = plates[l], plates[r]
    cnt[l_value] -= 1
    if cnt[l_value] == 0:
        del cnt[l_value]
    l += 1

    cnt[r_value] += 1
    r += 1
    r %= n

    ans = max(ans, len(cnt.keys()))

print(ans)
