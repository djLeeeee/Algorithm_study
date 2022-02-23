from sys import stdin as s

x, y = map(int, s.readline().split())
n = int(s.readline())

cycle = (x + y) * 2
position = []
for _ in range(n + 1):
    a, b = map(int, s.readline().split())
    if a == 2:
        position.append(b)
    elif a == 4:
        position.append(x + y - b)
    elif a == 1:
        position.append(2 * x + y - b)
    else:
        position.append(2 * x + y + b)
total = 0
for i in range(n):
    a = abs(position[i] - position[-1])
    total += min(a, cycle - a)
print(total)
