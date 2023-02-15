from sys import stdin

input = stdin.readline

n = int(input())
total = 0
color_sum = [0] * (n + 1)
ball = []
ans = [0] * n
for i in range(n):
    x, y = map(int, input().split())
    ball.append((y, x, i))
ball.sort(reverse=True)
while ball:
    size, color, i = ball.pop()
    ans[i] = total - color_sum[color]
    total += size
    color_sum[color] += size
    stack = 1
    while ball and ball[-1][0] == size and ball[-1][1] == color:
        _, _, j = ball.pop()
        ans[j] = total - color_sum[color]
        total += size
        color_sum[color] += size
        stack += 1
    while ball and ball[-1][0] == size:
        _, c, j = ball[-1]
        ex = 0
        while ball and ball[-1][0] == size and ball[-1][1] == c:
            _, _, j = ball.pop()
            ans[j] = total - color_sum[c] - stack * size
            total += size
            color_sum[c] += size
            ex += 1
        stack += ex
print(*ans, sep='\n')
