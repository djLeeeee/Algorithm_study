import sys
sys.stdin = open('input.txt')

n = int(input())
h_list = list(map(int, input().split()))
ans = [0] * n
stack = []

for i in range(n):
    h = h_list[i]
    # stack이 있고, 제일 마지막에 있는 애가 자신보다 낮으면 거기는 지나감
    while stack and stack[-1][0] <= h:
        stack.pop()
    if stack:
        ans[i] = stack[-1][1] +1
    stack.append((h, i))

print(*ans)

