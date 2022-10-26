def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n = int(input())
board = [list(input().split()) for _ in range(n)]
row = [[0] * n for _ in range(n)]
col = [[0] * n for _ in range(n)]
rn, cn = 0, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for x in range(n):
    for y in range(n):
        if board[x][y] == 'S':
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 'T':
                        print("NO")
                        exit()
                    else:
                        move = 0
                        while 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'X':
                            move += 1
                            nx += dx[d]
                            ny += dy[d]
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'T':
                            if d % 2:
                                cn += 1
                                for i in range(1, move + 1):
                                    col[x + dx[d] * i][y + dy[d] * i] = cn
                            else:
                                rn += 1
                                for i in range(1, move + 1):
                                    row[x + dx[d] * i][y + dy[d] * i] = rn
if rn <= 3 and cn <= 3:
    need = rn + cn
    graph = [[] for _ in range(rn + 1)]
    for x in range(n):
        for y in range(n):
            if row[x][y] and col[x][y]:
                graph[row[x][y]].append(col[x][y])
    match = [0] * (cn + 1)
    for i in range(1, rn + 1):
        visited = [False] * (cn + 1)
        need -= dfs(i)
        if need <= 3:
            print("YES")
            exit()
    else:
        print("NO")
else:
    print("NO")
