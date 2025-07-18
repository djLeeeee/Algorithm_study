# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/13904
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=13904&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

n = int(input())
prjs = [tuple(map(int, input().split())) for _ in range(n)]
prjs.sort()
day = prjs[-1][0] + 1
score = 0
hq = []
while day > 1:
    day -= 1
    while prjs and prjs[-1][0] >= day:
        d, w = prjs.pop()
        heappush(hq, -w)
    if hq:
        score += -heappop(hq)
print(score)
