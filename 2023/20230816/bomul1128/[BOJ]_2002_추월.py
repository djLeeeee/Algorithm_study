# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/2002
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=2002&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from sys import stdin

input = stdin.readline

n = int(input())
memo = {}
for i in range(n):
    x = input().rstrip()
    memo[x] = i
memo2 = {}
for i in range(n):
    x = input().rstrip()
    memo2[x] = i
keys = list(memo.keys())
ans = set()
for k1 in keys:
    for k2 in keys:
        if k1 in memo2 and k2 in memo2:
            if memo[k1] < memo[k2] and memo2[k1] > memo2[k2]:
                ans.add(k2)
print(len(ans))
