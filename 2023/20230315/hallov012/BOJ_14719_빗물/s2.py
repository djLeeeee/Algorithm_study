import sys
sys.stdin = open('input.txt')

h, w = map(int, input().split())
block = list(map(int, input().split()))
ans = 0
for i in range(1, w-1):
    left = max(block[:i])
    right = max(block[i+1:])
    b = min(left, right)
    if block[i] < b:
        ans += b - block[i]
print(ans)