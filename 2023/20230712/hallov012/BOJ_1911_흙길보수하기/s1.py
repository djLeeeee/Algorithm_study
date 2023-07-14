import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, l = map(int, input().split())
pools = [list(map(int, input().split())) for _ in range(n)]
pools.sort()
ans = 0
p = 0
for s, e in pools:
    if e <= p:
        continue
    if p <= s:
        p = s
    d = e - p
    if d % l:
        ans += d//l + 1
        p += l * (d // l + 1)
    else:
        ans += d//l
        p = e
print(ans)

