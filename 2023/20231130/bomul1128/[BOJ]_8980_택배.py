# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/8980
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=8980&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from sys import stdin

input = stdin.readline

town, limit = map(int, input().split())
n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
info.sort(key=lambda x: x[1])
ans = 0
luggage = [0] * town
for s, e, t in info:
    ml = max(luggage[s:e])
    ex = min(limit - ml, t)
    if ex:
        ans += ex
        for i in range(s, e):
            luggage[i] += ex
print(ans)
