# https://www.acmicpc.net/problem/7511
from collections import deque
import sys
sys.stdin = open("./input/7511.txt")
input = sys.stdin.readline

def BFS(s, e, n, nodes):
    visited = [0] * n
    que = deque([s])
    visited[s] = 1

    while que:
        ci = que.popleft()
        if ci == e:
            return 1
        for ni in nodes[ci]:
            if not visited[ni]:
                visited[ni] = 1
                que.append(ni)
    return 0

for test_case in range(int(input())):
    print("Scenario", test_case + 1)
    num_user = int(input())

    nodes = [[] for _ in range(num_user)]
    for _ in range(int(input())):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)
    
    for _ in range(int(input())):
        s, e = map(int, input().split())
        print(BFS(s, e, num_user, nodes))

