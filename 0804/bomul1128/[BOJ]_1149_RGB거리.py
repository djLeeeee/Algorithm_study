from sys import stdin

input = stdin.readline

a = int(input())
rgb = list(map(int, input().split()))
for _ in range(a - 1):
    r, g, b = map(int, input().split())
    rg = min(rgb[0], rgb[1])
    gb = min(rgb[1], rgb[2])
    br = min(rgb[0], rgb[2])
    rgb = [gb + r, br + g, rg + b]
print(min(rgb))
