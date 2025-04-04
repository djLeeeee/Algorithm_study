# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/13335
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=13335&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from collections import deque

n, l, w = map(int, input().split())
trucks = list(map(int, input().split()))
q = deque([0] * l)
time = 0
weight = 0
for truck in trucks:
    while True:
        time += 1
        weight -= q.popleft()
        if weight + truck <= w:
            q.append(truck)
            weight += truck
            break
        else:
            q.append(0)
print(time + l)
