# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/19598
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=19598&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from sys import stdin

input = stdin.readline

cnt = {}
for _ in range(int(input())):
    x, y = map(int, input().split())
    cnt[x] = cnt.get(x, 0) + 1
    cnt[y] = cnt.get(y, 0) - 1
ans = 0
tmp = 0
for k in sorted(cnt):
    tmp += cnt[k]
    ans = max(ans, tmp)
print(ans)
