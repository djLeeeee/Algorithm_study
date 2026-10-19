# Problem: https://school.programmers.co.kr/learn/courses/30/lessons/258711
# Submission: 2026-07-23 22:18:34 Python3 정답 100 /
def solution(edges):
    answer = [0, 0, 0, 0]
    n = 10 ** 6
    deg_in = [0] * (n + 1)
    deg_out = [0] * (n + 1)
    for x, y in edges:
        deg_in[y] += 1
        deg_out[x] += 1
    center = 0
    for i in range(1, n + 1):
        if deg_in[i] == 0 and deg_out[i] > 1:
            center = i
            break

    graph = [[] for _ in range(n + 1)]
    start = []
    for x, y in edges:
        if x == center:
            start.append(y)
        else:
            graph[x].append(y)
    visited = [False] * (n + 1)
    for v in start:
        donut = False
        cycle = False
        q = [v]
        for idx in q:
            if len(graph[idx]) == 2:
                donut = True
                break
            visited[idx] = True
            for adj in graph[idx]:
                if visited[adj]:
                    cycle = True
                else:
                    q.append(adj)
        if donut: # 8자
            answer[3] += 1
        elif cycle: # 도넛
            answer[1] += 1
        else:
            answer[2] += 1
    answer[0] = center
    return answer
