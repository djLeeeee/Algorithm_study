import sys
from collections import deque
sys.stdin = open('input.txt')

def dist(i, j):
    x1, y1 = enemy[i][0], enemy[i][1]
    x2, y2 = enemy[j][0], enemy[j][1]
    temp = (x1-x2)**2 + (y1-y2)**2
    return temp

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    enemy = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    ans = 0
    flag = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                d = dist(i, j)
                r = (enemy[i][2] + enemy[j][2]) ** 2
                if d <= r:
                    flag[i][j] = 1
    for i in range(n):
        if not visited[i]:
            ans += 1
            que = deque([i])
            visited[i] = 1
            while que:
                now = que.popleft()
                for next in range(n):
                    if now != next:
                        if flag[now][next] and not visited[next]:
                            que.append(next)
                            visited[next] = 1
    print(ans)