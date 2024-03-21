import sys
from collections import defaultdict
sys.stdin = open('input.txt')

l = input()
s = input().rstrip()
cnt = defaultdict(int)

for char in s:
    cnt[char] += 1

chars = ['A', 'C', 'G', 'T']
ans = 1
for char in chars:
    ans *= cnt[char]
print(ans % 1000000007)

