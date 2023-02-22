from sys import stdin
from collections import defaultdict

input = stdin.readline

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr += arr
cnt = defaultdict(int)
for i in range(k):
    cnt[arr[i]] += 1
cnt[c] += 1
tmp = ans = len(cnt)
for j in range(n - 1):
    cnt[arr[j]] -= 1
    if not cnt[arr[j]]:
        tmp -= 1
    if not cnt[arr[j + k]]:
        tmp += 1
    cnt[arr[j + k]] += 1
    if tmp > ans:
        ans = tmp
print(ans)
