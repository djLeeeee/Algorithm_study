# 백준 2584번 영역 구하기

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
def bfs(r, c):
    queue = [(r, c)]
    matrix[r][c] = 1
    cnt = 1

    while queue:
        cr, cc = queue.pop(0)
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < M and 0 <= nc < N and not matrix[nr][nc]:
                matrix[nr][nc] = 1
                queue.append((nr, nc))
                cnt += 1
    ans.append(cnt)


M, N, K = map(int, input().split())                 # M, N, K: 모눈종이의 세로, 가로의 길이 / 직사각형의 개수
matrix = [[0] * N for _ in range(M)]                # 모눈종이
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())      # (x1, y1): 왼쪽 아래 좌표, (x2, y2): 오른쪽 아래 좌표
    for r in range(M - y2, M - y1):
        for c in range(x1, x2):
            matrix[r][c] = 1                        # 직사각형 위치 표시
ans = []
for r in range(M):
    for c in range(N):
        if matrix[r][c] == 0:                       # 아직 살펴보지 않은 분리된 영역이면 bfs
            bfs(r, c)
print(len(ans))                                     # 분리되어 나누어지는 영역의 개수
print(*sorted(ans))                                 # 각 영역의 넓이를 오름차순으로 정렬