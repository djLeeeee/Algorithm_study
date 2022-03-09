import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(arr, start):
    num = [0]* N
    visited_list = [start]
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        for i in arr[x]:
            if i not in visited_list:
                num[i] = num[x] + 1
                queue.append(i)
                visited_list.append(i)

    return sum(num)

N, K = map(int, input().split())
arr = [[]*N for _ in range(N)]
visited = [[0]*N for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    arr[i-1].append(j-1)
    arr[j-1].append(i-1)
result = []
for i in range(N):
    result.append(bfs(arr, i))
print(result.index(min(result))+1)
