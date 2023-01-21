from sys import stdin

input = stdin.readline


def grounding(b, h):
    x = 0
    y = 0
    for i in range(257):
        if i > h:
            x += (i - h) * b[i]
        else:
            y += (h - i) * b[i]
    return 2 * x + y


a, b, inv = map(int, input().split())
block = [0] * 257
total_block = 0
M = 0
m = 256
for _ in range(a):
    for c in map(int, input().split()):
        total_block += c
        block[c] += 1
        if c < m:
            m = c
        if c > M:
            M = c

start = m
end = min((total_block + inv) // (a * b), M)
ans = grounding(block, start)
for i in range(start, end + 1):
    temp = grounding(block, i)
    if ans >= temp:
        height = i
        ans = temp
print(ans, height)
