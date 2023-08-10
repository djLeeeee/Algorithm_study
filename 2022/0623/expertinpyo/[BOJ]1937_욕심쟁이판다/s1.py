# 현재 방법 메모리 초과 발생
# 먼저 도는 점들에 대해 우선순위를 줘야할 듯

from collections import deque

def bfs(xx, yy):
    queue = deque()
    queue.append((xx, yy, 1))
    maxs = 1
    while queue:
        btn = False
        x, y, cnt = queue.popleft()
        maxs = max(cnt, maxs)
        for d in di:
            new_x, new_y = x + d[1], y + d[0]
            if 0 <= new_x < n and 0 <= new_y < n and arr[new_x][new_y] > arr[x][y]:
                btn = True
                if ansList[new_x][new_y]:
                    maxs = max(maxs, ansList[new_x][new_y] + cnt)
                else:
                    queue.append((new_x, new_y, cnt+1))
        if not btn: # 갈 곳이 없다면
            ansList[x][y] = 1
    ansList[xx][yy] = maxs


n = int(input())
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
arr = [list(map(int, input().split())) for _ in range(n)]

ansList = [[0] * n for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if not ansList[i][j]:
            bfs(i, j)
        ans = max(ans, ansList[i][j])
print(ans)



