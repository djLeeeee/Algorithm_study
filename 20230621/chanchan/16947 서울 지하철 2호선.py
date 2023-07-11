# https://www.acmicpc.net/problem/16947
import sys
from collections import deque
sys.stdin = open("./input/16947.txt")
input = sys.stdin.readline
# ----------------------------------------
N = int(input())
board = [[] for _ in range(N + 1)]

for _ in range(N):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

def check_cycle(n):
    que = deque([(0, n)])
    vst = [0] * (N + 1)
    vst[n] = 1

    while que:
        prev_node, cur_node = que.popleft()
        for next_node in board[cur_node]:
            cond1 = not vst[next_node]
            cond2 = prev_node != next_node
            if cond1 and cond2:
                vst[next_node] = 1
                que.append((cur_node, next_node))
            
            if not cond1 and cond2:
                return next_node
    
    return 0

cycles = [0] * (N + 1)
for n in range(1, N + 1):
    cycles[check_cycle(n)] = 1

print(cycles)

