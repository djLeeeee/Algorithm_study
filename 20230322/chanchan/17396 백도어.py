# https://www.acmicpc.net/problem/17396
import sys
import heapq
sys.stdin = open("input/17396.txt")
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    sights = list(map(int, input().split()))
    sights[-1] = 0
    record = [10e9] * N

    def back_door():
        q = []
        heapq.heappush(q, (0, 0))
        record[0] = 0
        while q:
            current_time, current_node = heapq.heappop(q)
            if record[current_node] < current_time:
                continue
            for next_node, next_time in graph[current_node]:
                cost = current_time + next_time
                if (cost < record[next_node] and not sights[next_node]):
                    record[next_node] = cost
                    heapq.heappush(q, (cost, next_node))

    for _ in range(M):
        a, b, t = map(int, input().split())
        graph[a].append((b, t))
        graph[b].append((a, t))
    
    back_door()
    
    answer = record[-1]
    if answer == 10e9:
        print(-1)
    else:
        print(answer)

    return

solution() 