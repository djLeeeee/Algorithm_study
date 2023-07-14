# 백준 1461번 도서관

import heapq
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
data = tuple(map(int, input().split()))
left = []
right = []
for d in data:
    if d < 0:
        left.append(d)
    else:
        right.append(d)
distance = []
left.sort()
for i in range(0, len(left), M):
    heapq.heappush(distance, abs(left[i]))
right.sort(reverse=True)
for j in range(0, len(right), M):
    heapq.heappush(distance, right[j])
print(distance)                             # heappush해도 작은 순으로 정렬되지 않음
ans = distance.pop()
while distance:
    ans += distance.pop() * 2
print(ans)