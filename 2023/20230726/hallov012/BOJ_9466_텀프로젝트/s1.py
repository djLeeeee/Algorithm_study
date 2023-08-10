import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def dfs(now):
    global cnt
    visited[now] = 1
    next = data[now]
    members.append(now)
    if visited[next]:
        if next in members:
            cnt += len(members) - members.index(next)
        return
    else:
        dfs(next)

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    data = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            members = []
            dfs(i)
    ans = n - cnt
    print(ans)