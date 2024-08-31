# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/4307
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=4307&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    arr = [int(input()) for _ in range(y)]
    a = 0
    b = 0
    for v in arr:
        v1 = min(v, x - v)
        v2 = max(v, x - v)
        if v1 > a:
            a = v1
        if v2 > b:
            b = v2
    print(a, b)
