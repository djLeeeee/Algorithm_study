# 백준 9205번 맥주 마시면서 걸어가기

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict, deque


def isHappy():
    queue = deque([0])
    visited[0] = 1

    while queue:
        cv = queue.popleft()
        for nv in dist[cv]:
            if not visited[nv]:
                visited[nv] = 1
                if nv == n + 1:
                    return "happy"
                queue.append(nv)
    return "sad"


t = int(input())
for tc in range(t):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n + 2)]
    dist = defaultdict(list)
    for i in range(n + 2):
        for j in range(n + 2):
            if i != j and abs(data[i][0] - data[j][0]) + abs(data[i][1] - data[j][1]) <= 1000:
                dist[i].append(j)
    visited = [0] * (n + 2)
    print(isHappy())