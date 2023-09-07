# https://www.acmicpc.net/problem/9205
import sys
from collections import deque
sys.stdin = open("./input/9205.txt")
input = sys.stdin.readline
# ----------------------------------------
def get_cord():
    i, j = map(int, input().split())
    return (i, j)


def can_go(si, sj, ei, ej):
    distance = abs(si - ei) + abs(sj - ej)
    return (distance <= 1000)


def BFS(si, sj, cords, vst, N):
    que = deque([(si, sj)])

    while (que):
        ci, cj = que.popleft()

        for ind in range(N + 1):
            ni, nj = cords[ind]
            if (can_go(ci, cj, ni, nj) and not vst[ind]):
                que.append((ni, nj))
                vst[ind] = 1
# ----------------------------------------
T = int(input())
for _ in range(T):
    N = int(input())
    si, sj = get_cord()

    cords = [0] * (N + 1)
    vst = [0] * (N + 1)

    for ind in range(N + 1):
        cords[ind] = get_cord()

    if (can_go(si, sj, cords[-1][0], cords[-1][1])):
        vst[N] = 1
    else:
        BFS(si, sj, cords, vst, N)

    print("happy" if vst[N] else "sad")