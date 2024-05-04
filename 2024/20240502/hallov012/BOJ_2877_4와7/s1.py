import sys
from collections import deque
sys.stdin = open('input.txt')

n = int(input())
ans = deque()

if n == 1:
    print(4)
elif n == 2:
    print(7)
else:
    while n:
        if n % 2:
            ans.appendleft(4)
        else:
            ans.appendleft(7)
            n -= 1
        n = n//2

    print(''.join(map(str, ans)))