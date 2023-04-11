import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
position = sorted(list(map(int, input().split())))
left, right = [], []
for p in position:
    if p < 0:
        left.append(p)
    else:
        right.append(p)
left.sort()
right.sort(reverse=True)

l, r = 0, 0
dist = []
while l < len(left):
    dist.append(-1 * left[l])
    l += m
while r < len(right):
    dist.append(right[r])
    r += m

dist.sort()
# 제일 먼 곳을 제일 마지막에 방문하고 0으로 돌아오지 않음
ans = dist.pop()
ans += sum(dist) * 2
print(ans)



