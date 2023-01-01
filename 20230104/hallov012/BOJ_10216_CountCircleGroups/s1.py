import sys
sys.stdin = open('input.txt')

def dist(i, j):
    x1, y1 = enemy[i][0], enemy[i][1]
    x2, y2 = enemy[j][0], enemy[j][1]
    temp = (x1-x2)**2 + (y1-y2)**2
    return temp

def dfs(now):
    for next in range(n):
        if now != next:
            if not visited[next] and dist(now, next) <= (enemy[now][2] + enemy[next][2])**2:
                visited[next] = 1
                dfs(next)

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    enemy = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    ans = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            ans += 1
    print(ans)