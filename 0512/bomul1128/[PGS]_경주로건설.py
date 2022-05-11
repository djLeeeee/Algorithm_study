import heapq


def solution(board):
    INF = float('inf')
    n = len(board)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    start = [(0, 0, 0, -1)]
    cost_table = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    cost_table[0][0] = [0, 0, 0, 0]
    while start:
        cost, x, y, curve = heapq.heappop(start)
        if x == y == n - 1:
            return cost
        if cost_table[x][y][curve] < cost:
            continue
        for i in range(4):
            new_cost = cost + 100
            nx = x + dx[i]
            ny = y + dy[i]
            if curve != -1 and curve != i:
                new_cost += 500
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if cost_table[nx][ny][i] > new_cost:
                    cost_table[nx][ny][i] = new_cost
                    heapq.heappush(start, (new_cost, nx, ny, i))
