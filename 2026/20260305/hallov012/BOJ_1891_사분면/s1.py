import sys
sys.stdin = open('input.txt')

d, start = map(str, input().split())
d = int(d)
a, b = map(int, input().split())

n = d
sx, sy = 0, 0
for s in start:
    n -= 1
    size = 2 ** n
    if s == '1':
        sy += size
    elif s == '2':
        pass
    elif s == '3':
        sx += size
    elif s == '4':
        sx += size
        sy += size

x, y = sx - b, sy + a
size = 2 ** d

if not 0 <= x < size or not 0 <= y < size:
    print(-1)
    exit()

ans = ''
for i in range(d):
    size = 2 ** (d-i)
    half = size // 2
    if 0 <= x < half:
        if half <= y:
            ans += '1'
            y -= half
        else:
            ans += '2'
    else:
        x -= half
        if y < half:
            ans += '3'
        else:
            ans += '4'
            y -= half
print(ans)
