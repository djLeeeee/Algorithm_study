# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/5397
from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
for _ in range(n):
    s = input().rstrip()
    left, right = deque(), deque()
    for c in s:
        if c == '<':
            if left:
                right.appendleft(left.pop())
        elif c == '>':
            if right:
                left.append(right.popleft())
        elif c == '-':
            if left:
                left.pop()
        else:
            left.append(c)
    left.extend(right)
    print(''.join(left))
