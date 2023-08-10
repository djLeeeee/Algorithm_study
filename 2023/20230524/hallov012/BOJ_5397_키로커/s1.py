import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    str = input().rstrip()
    left, right = deque(), deque()
    for char in str:
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
    if right:
        left += right
    print(''.join(left))



