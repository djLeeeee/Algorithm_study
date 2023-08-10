# https://www.acmicpc.net/problem/2610'
import sys
sys.stdin = open("./input/2610.txt")
input = sys.stdin.readline
from collections import deque
# ----------------------------------------
N = int(input())
K = int(input())

board = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
network = [[] for _ in range(N + 1)]

for _ in range(K):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

def bfs(n):
    vst = [0] * (N + 1) 
    group = [n]
    vst[n] = 1
    que = deque([(n, 0)])
    while que:
        cn, val = que.popleft()
        for next in network[cn]:
            if not vst[next]:
                group.append(next)
                vst[next] = 1
                board[n][cn][next] = val + 1
                que.append((next, val + 1 ))
    return group

checked = [0] * (N + 1)
groups = []
for n in range(1, N + 1):
    group = bfs(n)
    if checked[n]:
        continue

    for node in group:
        checked[node] = 1

    groups.append(group)
    


represents = []
for group in groups:
    top_val, top_num = sys.maxsize, 0
    for num in group:
        temp = 0
        for line in board[num]:
            temp += sum(line)

        if temp < top_val:
            top_val = temp
            top_num =  num
    represents.append(top_num)

ans_arr = sorted(list(set(represents)))
print(len(ans_arr))
print(*ans_arr, sep="\n")