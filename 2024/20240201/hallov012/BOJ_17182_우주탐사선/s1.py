import sys
sys.stdin = open('input.txt')

def dfs(now, p_cnt, d_cnt):
    global ans
    if d_cnt > ans:
        return
    if p_cnt == n:
        ans = d_cnt
        return
    for next in range(n):
        if not visited[next]:
            visited[next] = 1
            dfs(next, p_cnt+1, d_cnt+dist[now][next])
            visited[next] = 0

input = sys.stdin.readline

n, k = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(n)]

# 각 행성 간의 최소 거리 (중복으로 돌아다니는거 포함)
for t in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][t] + dist[t][j])

ans = sys.maxsize
visited = [0] * n
visited[k] = 1
dfs(k, 1, 0)

print(ans)