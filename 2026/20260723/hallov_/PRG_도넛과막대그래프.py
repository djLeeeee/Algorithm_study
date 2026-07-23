from collections import defaultdict, deque

def solution(edges):
    answer = [0, 0, 0, 0]
    out_g = defaultdict(int)
    in_g = defaultdict(int)
    g = defaultdict(list)
    nodes = set()

    for a, b in edges:
        out_g[a] += 1
        in_g[b] += 1
        nodes.add(a)
        nodes.add(b)
        g[a].append(b)

    node = 0
    # 나가는 것만 있으면 정점
    for x in nodes:
        if not in_g[x] and out_g[x] > 1:
            answer[0] = x
            node = x
            break

    m = 1000000
    visited = [0] * (m+1)
    for x in g[node]:
        visited[x] = 1
        cnt = 1
        edge_cnt = 0
        que = deque([x])
        flag = False
        while que:
            a = que.popleft()
            for b in g[a]:
                if b != node:
                    edge_cnt += 1
                    if not visited[b]:
                        visited[b] = 1
                        que.append(b)
                        cnt += 1
                    else:
                        flag = True
        # 8자
        if not flag:
            answer[2] += 1
        else:
            # 도넛
            if cnt == edge_cnt:
                answer[1] += 1
            # 막대
            elif cnt + 1 == edge_cnt:
                answer[3] += 1

    return answer
