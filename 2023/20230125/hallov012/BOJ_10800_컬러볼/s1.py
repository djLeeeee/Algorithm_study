import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
m = 200001
balls = []
for i in range(n):
    c, s = map(int, input().split())
    balls.append((c, s, i))
balls.sort(key=lambda x: x[1])
color_cnt = [0] * m
ans = [0] * n
total = 0

j = 0
for i in range(n):
    while balls[j][1] < balls[i][1]:
        color_cnt[balls[j][0]] += balls[j][1]
        total += balls[j][1]
        j += 1
    ans[balls[i][2]] = total - color_cnt[balls[i][0]]

for num in ans:
    print(num)


