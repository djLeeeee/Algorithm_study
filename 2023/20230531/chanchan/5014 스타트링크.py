# https://www.acmicpc.net/problem/5014
from collections import deque
import sys
sys.stdin = open("./input/5014.txt")
input = sys.stdin.readline
# ----------------------------------------
F, S, G, U, D = map(int, input().split())


vst = [0] * (F + 1)
vst[S] = 1

que = deque([S])

while (que):
    now = que.popleft()
    if (now == G):
        break

    for next in [now + U, now - D]:
        if (0 < next <= F and not vst[next]):
            que.append(next)
            vst[next] = vst[now] + 1


if (vst[G]):
    print(vst[G] - 1)
else:
    print("use the stairs")
