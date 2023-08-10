# 백준 5397번 키로거

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    string = input().rstrip()
    left, right = deque([]), deque([])
    for char in string:
        if char == '<':
            if left:
                right.appendleft(left.pop())
        elif char == '>':
            if right:
                left.append(right.popleft())
        elif char == '-':
            if left:
                left.pop()
        else:
            left.append(char)
    ans = ''
    print(*left, *right, sep='')
