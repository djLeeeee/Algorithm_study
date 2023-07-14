import sys
sys.stdin = open('input.txt')

# 마지막에 start로 돌아와야하므로 매개변수로 지정
def dfs(cnt, cost, start, now):
    global ans
    if cnt == n:
        # 돌아오는 길이 있는 경우 cost에 더해줌
        if g[now][start]:
            cost += g[now][start]
            ans = min(ans, cost)
        return
    if cost >= ans:
        return
    for j in range(1, n+1):
        if g[now][j] and not visited[j]:
            visited[j] = 1
            dfs(cnt+1, cost + g[now][j], start, j)
            visited[j] = 0

input = sys.stdin.readline

n = int(input())
g = [[0] * (n+1)]
for _ in range(n):
    row = [0] + list(map(int, input().split()))
    g.append(row)
visited = [0] * (n+1)
ans = sys.maxsize
for i in range(1, n+1):
    visited[i] = 1
    dfs(1, 0, i, i)
    visited[i] = 0
print(ans)

