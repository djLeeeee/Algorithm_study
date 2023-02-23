import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

input = sys.stdin.readline

def dfs(i):
    for j in g[i]:
        ans[j] += ans[i]
        dfs(j)

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
g = [[] for _ in range(n+1)]
for i in range(2, n+1):
    g[arr[i]].append(i)
ans = [0] * (n+1)
for _ in range(m):
    i, w = map(int, input().split())
    ans[i] += w

dfs(1)

print(*ans[1:])
