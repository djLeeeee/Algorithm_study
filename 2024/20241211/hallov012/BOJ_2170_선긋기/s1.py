import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
lines = sorted([list(map(int, input().split())) for _ in range(n)])
s, e = lines[0]

ans = 0
for i in range(1, n):
    x, y = lines[i]
    if x > e:
        ans += e - s
        s, e = x, y
    else:
        e = max(e, y)

ans += e - s
print(ans)