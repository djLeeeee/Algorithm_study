# 백준 15559번 내 선물을 받아줘

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution(r, c):
    global group
    stack = [(r, c)]
    visited[r][c] = group                   # 지금 위치에서 갈 수 있는 연결 위치 모두 group 숫자로 표시

    while stack:
        cr, cc = stack.pop()
        d = 0
        if data[cr][cc] == 'S':
            d = 1
        elif data[cr][cc] == 'W':
            d = 2
        elif data[cr][cc] == 'E':
            d = 3
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc]:         # 아직 방문하지 않았다면 연결된 위치
                visited[nr][nc] = group
                stack.append((nr, nc))
            elif visited[nr][nc] < group:   # 방문표시가 있는데 이전에 방문했다면 현재 살펴본 곳도 이전 group에 속함
                return 0                    # 선물 더 놓지 않아도 되므로 0 반환
    return 1


N, M = map(int, input().split())
data = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
group = ans = 0                             # group: 연결 된 장소를 표시할 변수, ans: 최소 선물 개수
for cr in range(N):
    for cc in range(M):
        if not visited[cr][cc]:
            group += 1
            ans += solution(cr, cc)
print(ans)