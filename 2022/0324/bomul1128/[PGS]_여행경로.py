from collections import defaultdict, deque


def solution(tickets):
    graph = defaultdict(list)
    for s, e in tickets:
        graph[s].append(e)
    for key in graph:
        graph[key].sort(reverse=True)
    stack = ['ICN']
    answer = deque()
    while stack:
        now = stack[-1]
        if graph[now]:
            adj = graph[now].pop()
            stack.append(adj)
        else:
            now = stack.pop()
            answer.appendleft(now)
    return answer
