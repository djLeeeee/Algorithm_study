from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [-1] * n
remain = [0]
for i in range(1, n):
    while remain and arr[remain[-1]] < arr[i]:
        ans[remain.pop()] = arr[i]
    remain.append(i)
print(*ans)
