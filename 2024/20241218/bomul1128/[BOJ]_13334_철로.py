# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/13334
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=13334&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
l = int(input())
points = []
INIT = 0
FIN = 1
for i, (x, y) in enumerate(arr):
    if x > y:
        x, y = y, x
    points.append((x, i, INIT))
    points.append((y, i, FIN))
points.sort()
ans = 0
tmp = 0
que = deque()
init_in_que = [0] * n
fin_in_que = [0] * n
for x, idx, state in points:
    while que and que[0][0] < x - l:
        _, i, s = que.popleft()
        if s == INIT:
            init_in_que[i] = 0
            tmp -= fin_in_que[i]
        else:
            fin_in_que[i] = 0
    que.append((x, idx, state))
    if state == INIT:
        init_in_que[idx] = 1
    else:
        tmp += init_in_que[idx]
        fin_in_que[idx] = 1
    if ans < tmp:
        ans = tmp
print(ans)
