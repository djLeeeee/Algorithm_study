"""
비트마스크: https://studyandwrite.tistory.com/325
&는 원소의 포함여부를 확인
"""
import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(i, j):
    que = deque([(i, j)])
    visited[i][j] = 1
    cnt = 1
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                # 해당 방향으로 벽이 없을 때, 그 위치로 이동
                if not 2**d & arr[x][y]:
                    visited[nx][ny] = 1
                    que.append((nx, ny))
                    cnt += 1
    return cnt

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
# 서 북 동 남
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
room_cnt = 0
max_cnt = 0
break_cnt = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            room_cnt += 1
            max_cnt = max(max_cnt, bfs(i, j))

for i in range(m):
    for j in range(n):
        k = 0
        while k < 4:
            # 벽이 있다면 벽을 부순다
            if 2**k & arr[i][j]:
                visited = [[0] * n for _ in range(m)]
                arr[i][j] -= 2**k
                break_cnt = max(break_cnt, bfs(i, j))
                # 초기화
                arr[i][j] += 2**k
            k += 1

print(room_cnt)
print(max_cnt)
print(break_cnt)
