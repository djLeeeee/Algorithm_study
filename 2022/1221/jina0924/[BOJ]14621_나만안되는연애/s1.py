# 백준 14621번 나만 안되는 연애

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq


def prim(v):
    heap = []
    heapq.heappush(heap, (0, v))
    dist = 0

    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            dist += w
            visited[v] = 1
            for w, weight in graph[v]:
                if univ[v] != univ[w] and not visited[w]:   # 서로 다른 성비의 대학교만 연결
                    heapq.heappush(heap, (weight, w))
    return dist


N, M = map(int, input().split())
univ = [0] + list(input().split())
graph = [[] * (N+1) for _ in range(N+1)]                    # 인접리스트
for _ in range(M):
    u, v, d = map(int, input().split())                     # u, v: 인접한 대학교, d: 그 거리
    graph[u].append((v, d))
    graph[v].append((u, d))
visited = [0] * (N+1)
ans = 987987987
result = prim(1)                                            # 1번 대학교부터 연결 시작
if sum(visited) != N:                                       # 모든 학교를 연결하는 경로 없다면 -1 출력
    print(-1)
    sys.exit()
if ans > result:
    ans = result
print(ans)