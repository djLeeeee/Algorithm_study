# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/2141
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=2141&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from sys import stdin

input = stdin.readline

n = int(input())
town = [tuple(map(int, input().split())) for _ in range(n)]
town.sort()
total = 0
for _, people in town:
    total += people
tmp = 0
ans = 0
for dist, people in town:
    tmp += people
    if tmp * 2 >= total:
        ans = dist
        break
print(ans)
