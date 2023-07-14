import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

def bfs(num, cnt):
    queue = deque()
    queue.append((num, cnt))
    while queue:
        num, cnt = queue.popleft()
        visited.append(num)
        for i in relationship[num]:
            if i == B:
                return cnt
            elif i not in visited:
                queue.append((i, cnt + 1))

N = int(input())
A, B = map(int, input().split())
relationship = defaultdict(list)
visited = [A]
M = int(input())
for _ in range(M):
    start, end = map(int, input().split())
    relationship[start].append(end)
    relationship[end].append(start)
answer = bfs(A, 1)
if not answer:
    answer = -1
print(answer)