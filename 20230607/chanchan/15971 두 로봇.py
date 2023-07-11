# https://www.acmicpc.net/problem/15971
from collections import deque
import sys
sys.stdin = open("./input/15971.txt")
input = sys.stdin.readline
# ----------------------------------------
N, start, end = map(int, input().split())

board = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b, dist = map(lambda x: int(x) - 1, input().split())
    board[a].append((b, dist + 1))
    board[b].append((a, dist + 1))

que = deque([(start - 1, 0, 0)])
vst = [0] * N
vst[start - 1] = 1

while que:
    cur_node, dist_tot, max_dist = que.popleft()
    if cur_node == end - 1:
        print(dist_tot - max_dist)
        exit()

    for (next_node, dist) in board[cur_node]:
        if not vst[next_node]:
            vst[next_node] = 1
            que.append((next_node, dist + dist_tot, max(dist, max_dist)))