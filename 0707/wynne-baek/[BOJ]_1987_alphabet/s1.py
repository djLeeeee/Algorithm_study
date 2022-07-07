import sys
sys.stdin = open('input.txt')

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
# print(board)
check = set(board[0][0])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 1

def dfs(dot, cnt):
    global answer
    answer = max(answer, cnt)
    x, y = dot
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in check:
            check.add(board[nx][ny])
            dfs((nx, ny), cnt + 1)
            check.remove(board[nx][ny])

start = (0, 0)
dfs((0, 0), 1)
print(answer)