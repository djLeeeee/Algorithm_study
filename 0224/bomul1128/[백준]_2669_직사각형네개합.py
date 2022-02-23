from sys import stdin as s

ground = [[0] * 100 for _ in range(100)]
for _ in range(4):
    x, y, x2, y2 = map(int, s.readline().split())
    for i in range(x, x2):
        for j in range(y, y2):
            ground[i][j] = 1
total = 0
for line in ground:
    total += sum(line)
print(total)
