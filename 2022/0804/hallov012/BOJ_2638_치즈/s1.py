import sys
from collections import deque
sys.stdin = open('input.txt')

# 가장자리는 치즈가 놓이지 않으므로 (0,0)부터 bfs를 돌려 공기에 노출된 공간을 표시한다
# data[x][y] == 1이라면 (x, y)는 공기에 노출된 공간
def blocked():
    data = [[0] * m for _ in range(n)]
    data[0][0] = 1
    que = deque([(0, 0)])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not data[nx][ny] and not arr[nx][ny]:
                    data[nx][ny] = 1
                    que.append((nx, ny))
    return data

def melt():
    blocked_arr = blocked()
    melt_lst = []
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n and 0 <= ny < m:
                        # 공기에 노출된 공간이 옆에 있다면 cnt += 1
                        if blocked_arr[nx][ny]:
                            cnt += 1
                if cnt >= 2:
                    melt_lst.append((i, j))
    # 치즈는 모든 구간을 탐색 후 한번에 녹인다
    for x, y in melt_lst:
        arr[x][y] = 0
    return

# 남은 치즈가 있는지 확인
def done():
    cnt = 0
    for line in arr:
        cnt += sum(line)
    if cnt:
        return False
    else:
        return True

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
while not done():
    melt()
    ans += 1

print(ans)