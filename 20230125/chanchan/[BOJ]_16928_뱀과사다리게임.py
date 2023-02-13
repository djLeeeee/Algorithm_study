# https://www.acmicpc.net/problem/16928
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
con = {}

for _ in range(N + M):
    x, y = map(int, input().split())
    con[x] = y

vst = [True] * 2 + [False] * 99
que = deque([(1, 0)])

s, e = 0, 1
while (s < e):
    cur_ind, cnt = que.popleft()
    if (cur_ind == 100):
        print(cnt)
        break
    
    cnt += 1

    for dice in range(1, 7):
        next_ind = cur_ind + dice
        if (next_ind > 100 or vst[next_ind]):
            continue
        
        vst[next_ind] = True
        if (next_ind in con):
            que.append((con[next_ind], cnt))
        else:
            que.append((next_ind, cnt))