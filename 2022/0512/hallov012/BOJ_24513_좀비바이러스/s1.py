import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * m for _ in range(n)]  # 전파된 시간대를 체크하기 위해 설정
que = deque()
for i in range(n):
    for j in range(m):
        if data[i][j] > 0:
            que.append((i, j))
            visited[i][j] = 1

while que:
    x, y = que.popleft()
    virus = data[x][y]
    if virus != 3:  # 3번은 더 이상 전염되지 않음
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != -1:  # 범위 안에 있고 치료제가 없는 마을일 때
                if not visited[nx][ny]:  # 전파된 바이러스가 아무 것도 없다면 전파한다
                    data[nx][ny] = virus
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
                else: # 이미 다른 바이러스가 전파되었을 때
                    if data[nx][ny] != virus and visited[nx][ny] == visited[x][y] + 1:
                        # 지금 전파될 바이러스와 다른 종류가 이미 전파되어 있고, 전파 시점이 같아 아직 완벽하게 감염되지 않은 상태일 때
                        if data[nx][ny] != 3: # 3번 바이러스에 다른 바이러스가 들어와도 3번임
                            data[nx][ny] = 3  # 그 마을을 3번 바이러스에 감염되었다고 바꿔줌 => 3번은 더 이상 감염되지 않으므로 append 하지 않음

ans = [0, 0, 0]
for i in range(n):
    for j in range(m):
        if data[i][j] in [1, 2, 3]:
            ans[data[i][j]-1] += 1
print(*ans)
