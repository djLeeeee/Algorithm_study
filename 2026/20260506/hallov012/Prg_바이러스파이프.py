from collections import deque

def solution(n, infection, edges, k):
    g = [[] for _ in range(n + 1)]
    for x, y, type in edges:
        g[x].append((y, type))
        g[y].append((x, type))

    visited = [0] * (n + 1)
    visited[infection] = 1

    answer = 1

    def bfs(visited, o_type):
        n_visited = visited[:]
        infected = [i for i in range(1, n + 1) if visited[i]]
        que = deque(infected)
        flag = False
        while que:
            now = que.popleft()
            for next, type in g[now]:
                if not n_visited[next] and type == o_type:
                    n_visited[next] = 1
                    que.append(next)
                    flag = True
        return n_visited, flag

    def dfs(visited, t, l_type):
        nonlocal answer
        answer = max(answer, sum(visited))
        for o_type in range(1, 4):
            n_visited, flag = bfs(visited, o_type)
            if not flag:
                continue
            n_t = t + (l_type != o_type)
            if n_t > k:
                continue
            dfs(n_visited, n_t, o_type)
    dfs(visited, 0, 0)

    return answer