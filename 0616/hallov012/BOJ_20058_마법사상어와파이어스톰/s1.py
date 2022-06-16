import sys
from collections import deque
sys.stdin = open('input.txt')

def rotate(l):
    new_data = [[0] * m for _ in range(m)]
    size = 2 ** l
    for i in range(0, m, size):
        for j in range(0, m, size):
            for x in range(size):
                for y in range(size):
                    new_data[i+x][j+y] = data[i+size-y-1][j+x]
    return new_data

def meting():
    # 녹을 얼음들의 위치 저장 (바로바로 녹게하면 그 다음 위치에서 판별할 때 오류가 생기기 때문에 마지막에 일괄적으로 처리)
    melt = []
    for i in range(m):
        for j in range(m):
            if data[i][j]:
                cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < m and 0 <= ny < m:
                        if data[nx][ny] > 0:
                            cnt += 1
                if cnt < 3:
                    melt.append((i, j))
    for x, y in melt:
        data[x][y] -= 1
    return

input = sys.stdin.readline

n, q = map(int, input().split())
m = 2 ** n
data = [list(map(int, input().split())) for _ in range(m)]
lvs = list(map(int, input().split()))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for l in lvs:
    data = rotate(l)
    meting()

total_ans = 0
max_ans = 0
for i in range(m):
    for j in range(m):
        if data[i][j]:
            total_ans += data[i][j]
            data[i][j] = 0
            cnt = 1
            que = deque([(i, j)])
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < m and 0 <= ny < m and data[nx][ny]:
                        total_ans += data[nx][ny]
                        cnt += 1
                        data[nx][ny] = 0
                        que.append((nx, ny))
            max_ans = max(max_ans, cnt)
print(total_ans)
print(max_ans)



