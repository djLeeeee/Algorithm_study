import sys, copy
from itertools import combinations
from collections import deque

sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, D = map(int, input().split())
origin_arr = [list(map(int, input().split())) for _ in range(n)]
# 궁수 기준으로 상, 좌, 우로만 탐색하면 됨
dx = [0, -1, 0]
dy = [-1, 0, 1]

ans = 0
positions = list(combinations(range(m), 3))

for position in positions:
    arr = copy.deepcopy(origin_arr)
    cnt = 0
    # 한칸씩 적이 내려오는게 아니라 궁수가 한칸씩 위로 올라감
    # 궁수랑 같은 줄에 있으면 쏠 수 없으니, 궁수의 한칸 위부터 시작
    for i in range(n-1, -1, -1):
        tmp = set()
        visited = [[0] * m for _ in range(n)]
        idx = 1
        for p in position:
            que = deque()
            que.append((i, p, 1))
            visited[i][p] = idx
            while que:
                x, y, d = que.popleft()
                if arr[x][y]:
                    tmp.add((x, y))
                    break
                if d < D:
                    for j in range(3):
                        nx = x + dx[j]
                        ny = y + dy[j]
                        if 0 <= nx < n and 0 <= ny < m:
                            if visited[nx][ny] != idx:
                                visited[nx][ny] = idx
                                que.append((nx, ny, d+1))
            idx += 1
        cnt += len(tmp)
        for x, y in tmp:
            arr[x][y] = 0
    ans = max(ans, cnt)

print(ans)




