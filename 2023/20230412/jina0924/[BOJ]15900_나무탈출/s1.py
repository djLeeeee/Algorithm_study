# 백준 15900번 나무 탈출

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict, deque

N = int(input())
tree = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
cnt = 0
leaves = deque([1])
visited = [0] * (N + 1)
visited[1] = 1
while leaves:
    node = leaves.popleft()
    depth = visited[node]
    if node != 1 and len(tree[node]) == 1:
        cnt += depth - 1
    for neighbor in tree[node]:
        if not visited[neighbor]:
            leaves.append(neighbor)
            visited[neighbor] = depth + 1
print("Yes" if cnt % 2 else "No")