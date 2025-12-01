import sys
sys.stdin = open('input.txt')

def count(lst):
    cnt = 0
    for x in lst:
        for y in lst:
            cnt += arr[x][y]
    return cnt

def dfs(cnt, p, idx):
    global ans
    if cnt == p:
        link = []
        start = []
        for i in range(1, n+1):
            if visited[i]:
                link.append(i)
            else:
                start.append(i)
        tmp1 = count(link)
        tmp2 = count(start)
        ans = min(ans, abs(tmp1 - tmp2))
        return
    for i in range(idx+1, n+1):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt+1, p, i)
            visited[i] = 0

input = sys.stdin.readline

n = int(input())
arr = [[0] * (n+1)]
for _ in range(n):
    line = [0] + list(map(int, input().split()))
    arr.append(line)
ans = sys.maxsize
for i in range(1, n):
    visited = [0] * (n+1)
    dfs(0, i, 0)

print(ans)