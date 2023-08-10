from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    inf = 987654321
    cost = [[inf] * n for _ in range(n)]
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]
    cost[0][0] = 0
    que = deque([(0, 0, 0, 5)]) # (x, y, value, d)  d:이전에 움직였던 방향, 초기엔 이전 방향이 없으므로 5로 설정
    while que:
        x, y, value, d = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                if d == 5 or d == i:  # 이전에 도로를 세운것과 같은 방향이었으면 직선도로
                    if value + 1 <= cost[nx][ny]:
                        cost[nx][ny] = value + 1
                        que.append((nx, ny, cost[nx][ny], i))
                else:  # 다른 방향이었다면 커브를 건설하는 것
                    if value + 6 <= cost[nx][ny]:
                        cost[nx][ny] = value + 6
                        que.append((nx, ny, cost[nx][ny], i))
    answer = cost[-1][-1] * 100
    return answer

print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))