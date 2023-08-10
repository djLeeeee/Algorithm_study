import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union_set(x, y):
    p[find_set(y)] = find_set(x)


def kruskal():
    idx = cnt = 0
    # 도달하지 못하는 경우도 있다.
    # 그럴 경우에 cnt는 늘어나지 않는데 idx는 계속해서 늘어나기 때문에 IndexError가 뜬다.
    # 따라서 and 뒷부분을 추가해주었다.
    # 이런 엣지 케이스를 주의하도록 하자!
    while cnt < N - 1 and idx < M:
        x = edges[idx][0]
        y = edges[idx][1]
        weight = edges[idx][2]
        if find_set(x) != find_set(y):
            union_set(x, y)
            cnt += 1
            # 매번 유니온 검사 후 같아지면 즉시 리턴
            if find_set(start) == find_set(end):
                return weight
        idx += 1
    return 0


# 1. 노드의 개수 N, 간선의 개수 M

N, M = map(int, input().strip().split())

p = [i for i in range(N+1)]

# 2. 출발지와 끝 => 최대값부터 내림차순으로 진행되니 같은 집합에 속하는 즉시 끝내면 그 최소값을 리턴
start, end = map(int, input().strip().split())
edges = []

for i in range(M):
    edge = list(map(int, input().strip().split()))
    edges.append(edge)


# 3. 최대값순으로 정렬
edges.sort(reverse=True, key=lambda x: x[2])

print(kruskal())

# kruskal을 최소 비용 순이 아니라 최대 비용(가져갈 수 있는 막대기 수)으로 돌리는 거다.
# dfs가 필요할까 생각했는데, 그럴 필요 없이 같은 그룹에 속하면 그대로 종료하면 된다.
