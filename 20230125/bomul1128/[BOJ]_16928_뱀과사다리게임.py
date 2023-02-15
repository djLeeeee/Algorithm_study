from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
moving = list(range(101))
dist = [-1] * 101
for _ in range(m + n):
    x, y = map(int, input().split())
    moving[x] = y
ans = 0
dist[1] = 0
point = [1]
for idx in point:
    t = dist[idx]
    for ex in range(1, 7):
        if idx + ex >= 100:
            dist[100] = t + 1
            break
        adj = moving[idx + ex]
        if dist[adj] == -1:
            dist[adj] = t + 1
            point.append(adj)
    else:
        continue
    break
print(dist[100])
