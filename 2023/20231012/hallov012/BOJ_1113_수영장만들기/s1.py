import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0
# 물의 높이는 최대 8
for h in range(1, 9):
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] <= h:
                que = deque([(i, j)])
                visited[i][j] = 1
                cnt = 1
                flag = True
                while que:
                    x, y = que.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if not visited[nx][ny] and arr[nx][ny] <= h:
                                visited[nx][ny] = 1
                                que.append((nx, ny))
                                cnt += 1
                        # 물이 넘친다는 거니까 물을 채울 수 없음, 그리고 연결된 부분은 체크
                        else:
                            flag = False
                            continue
                if flag:
                    ans += cnt

print(ans)