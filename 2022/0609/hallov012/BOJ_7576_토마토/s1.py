import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

m, n = map(int, input().split())
data = []
# 익지 않은 토마토의 수를 저장
cnt = 0
que = deque()
visited = [[0] * m for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 1:
            que.append((i, j))
            visited[i][j] = 1
        elif line[j] == 0:
            cnt += 1
    data.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
# 만약 익지 않은 토마토가 없는 경우 ans 출력 후 코드 종료
if cnt == 0:
    print(ans)
    exit()

while True:
    ans += 1
    # 오늘 익은 토마토들을 새로운 que 에 저장
    new_que = deque()
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and data[nx][ny] == 0:
                    # 새로운 토마토가 익었다면 cnt 를 줄여준다
                    cnt -= 1
                    visited[nx][ny] = 1
                    new_que.append((nx, ny))
    # 익지 않은 토마토가 없다면 탈출
    if cnt == 0:
        break
    else:
        if new_que:
            que = new_que
        # 오늘 아무런 토마토도 익지 않았다면 모든 토마토가 익는 경우가 없다고 보고 종료
        else:
            ans = -1
            break

print(ans)




