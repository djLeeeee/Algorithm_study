from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())
cnt = defaultdict(int)
for _ in range(n):
    word = input().strip()
    l = len(word)
    for i in range(l):
        cnt[word[i]] += 10 ** (l - i - 1)
value = sorted(cnt.values(), reverse=True)
ans = 0
c = 9
for v in value:
    ans += c * v
    c -= 1
print(ans)
