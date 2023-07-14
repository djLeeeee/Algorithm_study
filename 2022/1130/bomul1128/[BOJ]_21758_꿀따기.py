n = int(input())
arr = list(map(int, input().split()))
prefix = [0] * n
prefix[0] = arr[0]
for i in range(1, n):
  prefix[i] = prefix[i - 1] + arr[i]
ans = prefix[-2] - prefix[0] + max(arr[1:-1])
for i in range(1, n - 1):
  temp = 2 * prefix[-1] - arr[0] - prefix[i] - arr[i]
  if temp > ans:
    ans = temp
  temp = prefix[-2] + prefix[i - 1] - arr[i]
  if temp > ans:
    ans = temp
print(ans)
