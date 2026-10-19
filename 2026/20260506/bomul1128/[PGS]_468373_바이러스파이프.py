# Problem: https://school.programmers.co.kr/learn/courses/30/lessons/468373
# Submission: 2026-05-14 17:03:15 Python3 정답 100 /
def solution(n, infection, edges, k):
    def check(first, bits):        
        visited = [False] * (n + 1)
        visited[infection] = True
        que = [infection]
        for idx in que:
            for adj, t in tree[idx]:
                if t == first and not visited[adj]:
                    que.append(adj)
                    visited[adj] = True
        opened = first
        for i in range(k - 1):
            opened += 1 + (bits >> i & 1)
            opened %= 3
            for idx in que:
                for adj, t in tree[idx]:
                    if not visited[adj] and t == opened:
                        que.append(adj)
                        visited[adj] = True
        return len(que)
    
    graph = [[] for _ in range(n + 1)]
    for x, y, t in edges:
        graph[x].append((y, t - 1))
        graph[y].append((x, t - 1))
    visited = [False] * (n + 1)
    visited[infection] = True
    tree = [[] for _ in range(n + 1)]
    stack = [infection]
    while stack:
        idx = stack.pop()
        for adj, t in graph[idx]:
            if not visited[adj]:
                tree[idx].append((adj, t))
                visited[adj] = True
                stack.append(adj)
    del graph

    answer = 0
    for f in range(3):
        for bits in range(1 << (k - 1)):
            tmp = check(f, bits)
            if tmp > answer:
                answer = tmp
    return answer
