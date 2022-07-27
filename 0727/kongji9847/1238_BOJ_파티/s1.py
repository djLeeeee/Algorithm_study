'''
최단 거리 구하기 - 다익스트라 알고리즘 사용
왕복 최단 거리 - Node1 -> X: 시작 지점을 X로 하고 단일방향 간선을 역방향으로 돌려서 다익스트라 사용하기
1 → 3 → 5 == 1 ← 3 ← 5
'''

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 2. 다익스트라 함수 구현
import heapq
def dijkstra(start, roads):
    global time_sum
    visited = [0] * (N+1)
    heap = []
    heapq.heappush(heap, (0, start))
    cnt = 0                                                                         # 모든 노드를 방문했는지 확인하는 변수 - heap이 비워질 때까지 돌아가는 것 막기

    while heap and cnt < N:
        t, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            time_sum[node] += t
            cnt += 1
            for next in range(1, N+1):
                if not visited[next]:
                    heapq.heappush(heap, (t + roads[node][next], next))             # 누적 가중치를 포함해서 heap에 넣어줌(heap에는 항상 시작(목표)지점과 node의 가중치만이 들어있게 한다.)

    return time_sum


# 0. input 및 road(graph)만들기
N, M, X = map(int, input().split())
roads = [[987654321]*(N+1) for _ in range(N+1)]
for _ in range(M):
    S, E, T = map(int, input().split())
    roads[S][E] = T
for i in range(N+1):
    roads[i][i] = 0

# 1. 왕복 시간 합을 담을 배열과 출발과 시작이 반대로 된 graph 만들기
time_sum = [0] * (N+1)
invert_roads = list(zip(*roads))

dijkstra(X, roads)
dijkstra(X, invert_roads)

# 3. 답 출력
print(max(time_sum))