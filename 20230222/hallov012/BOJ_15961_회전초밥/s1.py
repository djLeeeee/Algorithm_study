import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
ans = 0

left, right = 0, k-1
temp = defaultdict(int)
for i in range(k):
    temp[arr[i]] += 1
temp[c] += 1

while left < n:
    if len(temp) >= d:
        print(len(temp))
        exit()
    ans = max(ans, len(temp))
    temp[arr[left]] -= 1
    if not temp[arr[left]]:
        del temp[arr[left]]
    left += 1
    right += 1
    temp[arr[right % n]] += 1

print(ans)
