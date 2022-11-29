import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
while True:
    visited = [[0] * n for _ in range(n)]
    # 국경선이 여는 나라가 있는지 확인하는 flag
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                # cnt: 국경선을 여는 나라들의 인구 총합, union: 국경선을 여는 나라들의 위치
                cnt = arr[i][j]
                union = [(i, j)]
                que = deque([(i, j)])
                visited[i][j] = 1
                while que:
                    x, y = que.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if not visited[nx][ny] and l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                                union.append((nx, ny))
                                cnt += arr[nx][ny]
                                visited[nx][ny] = 1
                                que.append((nx, ny))
                # 다른 나라와 국경을 여는 경우
                if len(union) > 1:
                    flag = True
                    temp = cnt // len(union)
                    for x, y in union:
                        arr[x][y] = temp
    if not flag:
        break
    ans += 1
print(ans)
