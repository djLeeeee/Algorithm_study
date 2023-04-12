# 백준 1461번 도서관

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
    distance.append(abs(left[i]))
right.sort(reverse=True)
for j in range(0, len(right), M):
    distance.append(right[j])
distance.sort()
ans = distance.pop()
while distance:
    ans += distance.pop() * 2
print(ans)