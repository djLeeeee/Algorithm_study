import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
n = 10000
for _ in range(T):
    a, b = map(int, input().split())
    visited = [''] * n
    visited[a] = '.'
    que = deque([a])
    while que:
        x = que.popleft()
        if x == b:
            print(visited[x][1:])
            break
        s, e = x // 1000, x % 10
        nums = {
            'D': (x * 2) % n,
            'S': (x - 1) % n,
            'L': (x % 1000) * 10 + s,
            'R': 1000 * e + (x // 10)
        }

        for order, val in nums.items():
            if not visited[val]:
                visited[val] = visited[x] + order
                que.append(val)

