import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

tc = 0
while True:
    tc += 1
    n = int(input())
    if not n:
        break
    data = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 최솟값을 찾을 예정이므로 maxsize로 구성
    visited = [[sys.maxsize] * n for _ in range(n)]
    visited[0][0] = -1
    que = deque([(0, 0, data[0][0])])
    while que:
        x, y, loss = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if loss + data[nx][ny] < visited[nx][ny]:
                    visited[nx][ny] = loss + data[nx][ny]
                    que.append((nx, ny, loss + data[nx][ny]))
    print(f'Problem {tc}: {visited[n-1][n-1]}')

