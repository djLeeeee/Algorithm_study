import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = []
total = 0

for _ in range(n):
    x, a = map(int, input().split())
    total += a
    data.append((x, a))

data.sort()
cnt = 0
for x, a in data:
    cnt += a
    if cnt >= total / 2:
        print(x)
        exit()

