import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def dfs(node, cnt):
    global ans, max_node
    if cnt > ans:
        ans = cnt
        max_node = node
    for e, d in g_dic[node]:
        if not visited[e]:
            visited[e] = 1
            dfs(e, cnt+d)
            visited[e] = 0

input = sys.stdin.readline

v = int(input())
g_dic = defaultdict(list)
for _ in range(v):
    data = list(map(int, input().split()))
    start = data[0]
    for i in range(1, len(data)-1, 2):
        end, d = data[i], data[i+1]
        g_dic[start].append([end, d])

visited = [0] * (v+1)
ans = 0
max_node = 0

# 임의의 노드 1부터 가장 먼 max_node 구하기
visited[1] = 1
dfs(1, 0)
# max_node에서부터 제일 먼 거리를 구하면 그 값이 트리의 지름
visited = [0] * (v+1)
visited[max_node] = 1
dfs(max_node, 0)
print(ans)