# 백준 1261번 알고스팟

import sys
sys.stdin = open('input3.txt')
import heapq

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
def smash():
    heap = []                                       # 최소 횟수 구하기 위해 힙 사용
    heapq.heappush(heap, (0, 0, 0))
    visited[0][0] = 1

    while heap:
        cnt, r, c = heapq.heappop(heap)
        if r == n-1 and c == m-1:
            return cnt
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                # heappop했을 때 visited를 갱신해주면 시간초과 남
                # 어차피 최소 횟수 만큼 벽 부수면서 이동하므로 새 위치 찾았을 때 갱신해줘도 상관x
                visited[nr][nc] = 1
                if maze[nr][nc]:
                    heapq.heappush(heap, (cnt+1, nr, nc))
                elif maze[nr][nc] == 0:
                    heapq.heappush(heap, (cnt, nr, nc))


m, n = map(int, input().split())                        # m: 가로 크기, n: 세로 크기
maze = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]                   # 방문 표시
print(smash())