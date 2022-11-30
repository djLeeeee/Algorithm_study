from sys import stdin

input = stdin.readline

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while True:
  flag = False
  visited = [[False] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if visited[i][j]:
        continue
      visited[i][j] = True
      point = [(i, j)]
      check = [(i, j)]
      cnt = board[i][j]
      while point:
        x, y = point.pop()
        for d in range(4):
          nx = x + dx[d]
          ny = y + dy[d]
          if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if l <= abs(board[nx][ny] - board[x][y]) <= r:
              visited[nx][ny] = True
              cnt += board[nx][ny]
              check.append((nx, ny))
              point.append((nx, ny))
      if len(check) > 1:
        flag = True
        new = cnt // len(check)
        for x, y in check:
          board[x][y] = new
  if flag:
    ans += 1
  else:
    break
print(ans)
