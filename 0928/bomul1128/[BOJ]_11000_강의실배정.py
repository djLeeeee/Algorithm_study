from heapq import *

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
ans = 0
point = 0
stack = []
while point < n:
    x, y = arr[point]
    while point < n and arr[point][0] == x:
        heappush(stack, arr[point][1])
        point += 1
    while stack and stack[0] <= x:
        heappop(stack)
    if len(stack) > ans:
        ans = len(stack)
print(max(ans, len(stack)))
