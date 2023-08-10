import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, k, m = map(int, input().split())
data = []
for _ in range(n):
    l = int(input())
    if l > 2*k:
        data.append(l - 2*k)
    elif 2*k > l > k:
        data.append(l-k)

if not data:
    print(-1)
    exit()

left, right = 1, max(data)
ans = -1
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for num in data:
        cnt += num//mid
    if cnt < m:
        right = mid-1
    else:
        left = mid+1
        ans = mid

print(ans)