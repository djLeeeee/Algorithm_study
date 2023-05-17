# https://www.acmicpc.net/problem/1325 => pypy3로 통과
from collections import deque
import sys
sys.stdin = open("./input/1325.txt")
input = sys.stdin.readline
# ----------------------------------------

N, M = map(int, input().split())
childs = {}

for _ in range(M):
    node1, node2 = map(int, input().split())
    childs[node2] = childs.get(node2, []) + [node1]

memo = [0] * (N + 1)
def dfs(node):
    if memo[node]:
        return memo[node]
    
    que = deque([node])
    vst = [0] * (N + 1)
    vst[node] = 1
    temp = 0
    while que:
        cur_node = que.popleft()
        temp += 1
        for next_node in childs.get(cur_node, []):
            if not vst[next_node]:
                vst[next_node] = 1
                que.append(next_node)
    return temp

max_val, max_arr = 0, []
for node in childs:
    cnt = dfs(node)
    if cnt > max_val:
        max_val = cnt
        max_arr = [node]
    elif cnt == max_val:
        max_arr.append(node)
    memo[node] = cnt

ans = sorted(max_arr)
print(*ans)