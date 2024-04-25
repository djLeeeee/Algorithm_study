import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
under, upper = [], []

cnt = 0
for num in nums:
    if num < 1:
        under.append(num)
    elif num > 1:
        upper.append(num)
    else:
        # 어차피 1은 곱하면 사라지니까, 그냥 더해주는게 이득
        cnt += 1

under.sort()
upper.sort(reverse=True)


x, y = len(under), len(upper)

for i in range(x//2):
    cnt += under[2*i] * under[2*i + 1]
if x % 2:
    cnt += under[-1]

for j in range(y//2):
    cnt += upper[2*j] * upper[2*j + 1]
if y % 2:
    cnt += upper[-1]

print(cnt)