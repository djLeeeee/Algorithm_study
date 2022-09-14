# 백준 17472_다리만들기2

import sys
sys.stdin = open('input3.txt')
from collections import deque
import heapq


def island(r, c):                           # 인접한 섬 같은 수로 만들기
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and data[nr][nc] == 1:
                data[nr][nc] += cnt
                queue.append((nr, nc))


def prim():                                 # 최소 신장 트리 구하기
    ans = 0
    heap = []
    heapq.heappush(heap, (0, 2))
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            ans += w
            visited[v] = 1
            for node, weight in G[v]:
                if not visited[node]:
                    heapq.heappush(heap, (weight, node))
    return ans


N, M = map(int, input().split())            # N: 지도의 세로 길이, M: 지도의 가로 길이
data = [list(map(int, input().split())) for _ in range(N)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
cnt = 0
for r in range(N):                          # 섬 구분해주기
    for c in range(M):
        if data[r][c] == 1:                 # 데이터 값이 1일 때 = 섬
            cnt += 1
            data[r][c] += cnt               # 방문한 곳과 구분짓기 위해 연결된 섬을 같은 수를 더해줌
            island(r, c)
visited = [0] * (cnt+2)                     # 방문표시
G = [[] for _ in range(cnt+2)]              # 인접리스트
for r in range(N):                          # 행에서 만들 수 있는 다리 정보 저장하기
    sv = 0
    sc = 0
    for c in range(M):
        if data[r][c]:
            if sv and data[r][c] != sv:
                if c - sc - 1 > 1:
                    G[sv].append([data[r][c], c - sc - 1])
                    G[data[r][c]].append([sv, c - sc - 1])
            sc, sv = c, data[r][c]
for c in range(M):                          # 열에서 만들 수 있는 다리 정보 저장하기
    sv = 0
    sr = 0
    for r in range(N):
        if data[r][c]:
            if sv and data[r][c] != sv:
                if r - sr - 1 > 1:
                    G[sv].append([data[r][c], r - sr - 1])
                    G[data[r][c]].append([sv, r - sr - 1])
            sr, sv = r, data[r][c]
result = prim()                             # 최소 신장 트리 찾기
if sum(visited) != cnt:                     # 모든 곳을 방문하지 못했다면 섬 연결 x
    print(-1)
else:
    print(result)