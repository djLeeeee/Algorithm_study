m, n, k = map(int, input().split())

answer = 0
areas = []
board = list([[1] * (m) for _ in range(n)])

for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    for x in range(sx, ex):
        for y in range(sy, ey):
            board[x][y] = 0

delta = list(zip([1, -1, 0, 0], [0, 0, 1, -1]))

def isInArea(x, y, board, m, n):
    isInBorder = (0 <= x < n) and (0 <= y < m)
    if (isInBorder and board[x][y] == 1):
        return True
    return False
    

def goBFS(x, y, board):
    board[x][y] = 0

    que = [(x, y)]
    s, e = 0, 1

    while (s < e):
        ex, ey = que[s]
        s += 1
        
        for (dx, dy) in delta:
            nx, ny = ex + dx, ey + dy
            if (isInArea(nx, ny, board, m, n)):
                board[nx][ny] = 0
                que.append((nx, ny))
                e += 1
    
    return len(que)



for x in range(n):
    for y in range(m):
        if board[x][y]:
            answer += 1
            area = goBFS(x, y, board)
            areas.append(area)

areas.sort()

print(answer)
print(*areas, " ")
