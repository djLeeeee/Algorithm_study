import sys
from collections import deque
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def find(node):
    global ans
    p, l, r = g[node]

    # 현재 node의 왼쪽 자식들을 순회해서 그 수를 count
    cnt = 1
    visited[node] = 1
    if l != -1:
        ans += 2
        que = deque([l])
        while que:
            x = que.popleft()
            a, b, c = g[x]
            for y in (b, c):
                if y != -1 and not visited[y]:
                    visited[y] = 1
                    cnt += 1
                    que.append(y)
    ans += 2 * (cnt-1)

    # 오른쪽으로 탐색 할 수 있다면 r을 node로 다시 한번 반복
    if r != -1:
        ans += 1
        find(r)

input = sys.stdin.readline

n = int(input())
g = [[-1, -1, -1] for _ in range(n+1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    g[b][0] = g[c][0] = a
    g[a][1] = b
    g[a][2] = c

ans = 0
visited = [0] * (n+1)
node = 1
find(node)
print(ans)


