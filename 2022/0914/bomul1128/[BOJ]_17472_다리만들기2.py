from heapq import heappop, heapify


def find(t: int) -> int:
    if t == p[t]:
        return t
    p[t] = find(p[t])
    return p[t]


def union(a: int, b: int) -> None:
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


def dfs(a: int, b: int) -> None:
    board[a][b] = idx
    for d in range(4):
        na = a + dx[d]
        nb = b + dy[d]
        if 0 <= na < n and 0 <= nb < m and board[na][nb] == '1':
            dfs(na, nb)


n, m = map(int, input().split())
board = []
idx = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
board = [input().rstrip().split() for _ in range(n)]
for x in range(n):
    for y in range(m):
        if board[x][y] == '1':
            idx += 1
            dfs(x, y)
p = list(range(idx + 1))
bridge = set()
for xx in range(n):
    for yy in range(m):
        if board[xx][yy] != '0':
            for dd in range(4):
                nx, ny = xx, yy
                cost = 0
                nx += dx[dd]
                ny += dy[dd]
                while 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '0':
                    cost += 1
                    nx += dx[dd]
                    ny += dy[dd]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != '0' and cost > 1:
                    bridge.add((cost, board[xx][yy], board[nx][ny]))
bridge = list(bridge)
heapify(bridge)
edge = 0
total = 0
while edge < idx - 1 and bridge:
    c, init, fin = heappop(bridge)
    if find(init) != find(fin):
        union(init, fin)
        total += c
        edge += 1
if bridge:
    print(total)
else:
    print('-1')
