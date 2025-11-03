import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
g = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
order = list(map(int, input().split()))

if order[0] != 1:
    print(0)
    exit()

stack = [order[0]]
for i in range(1, n):
    val = order[i]
    while stack and val not in g[stack[-1]]:
        stack.pop()
        if not stack:
            print(0)
            exit()
    stack.append(val)

print(1)

