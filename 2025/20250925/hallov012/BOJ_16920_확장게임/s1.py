import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, p = map(int, input().split())
s_lst = [0] + list(map(int, input().split()))
castle = [[] for _ in range(p+1)]
castle_cnt = [0] * (p+1)
arr = [[0] * m for _ in range(n)]
for i in range(n):
    row = input()
    for j in range(m):
        if row[j] != '.' and row[j] != '#':
            player = int(row[j])
            arr[i][j] = player
            castle[player].append((i, j))
            castle_cnt[player] += 1
        else:
            arr[i][j] = -1 if row[j] == '#' else 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while True:
    new = 0
    for i in range(1, p+1):
        s = s_lst[i]
        next = []
        while s and castle[i]:
            for x, y in castle[i]:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
                        arr[nx][ny] = i
                        castle_cnt[i] += 1
                        new += 1
                        next.append((nx, ny))
            castle[i] = next
            next = []
            s -= 1
    if not new:
        break

print(*castle_cnt[1:])




