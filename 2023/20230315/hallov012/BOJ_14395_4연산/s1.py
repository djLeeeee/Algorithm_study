import sys
from collections import deque
sys.stdin = open('input.txt')


s, t = map(int, input().split())
que = deque([(s, '')])
n = 10 ** 9
visited = set()
visited.add(s)
if s == t:
    print(0)
    exit()
while que:
    num, val = que.popleft()
    if num == t:
        print(val)
        break
    next = {'*': num*num, '+': num*2, '/': 1}
    for oper, value in next.items():
        if 0 <= value <= n and not value in visited:
            visited.add(value)
            que.append((value, val+oper))
else:
    print(-1)