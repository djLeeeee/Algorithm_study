import sys
sys.stdin = open('input.txt')

def find_dist():
    cnt = 0
    for i in range(a):
        dist = 2 * n
        for j in range(b):
            if not closed[j]:
                if dist > dist_arr[i][j]:
                    dist = dist_arr[i][j]
        cnt += dist
    return cnt

def dfs(idx, close):
    global ans
    if close == close_cnt:
        cnt = find_dist()
        ans = min(cnt, ans)
        return
    for i in range(idx, b):
        if not closed[i]:
            closed[i] = 1
            dfs(i, close+1)
            closed[i] = 0

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
homes, stores = [], []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            homes.append((i, j))
        elif arr[i][j] == 2:
            stores.append((i, j))
close_cnt = len(stores) - m
ans = 2 * n * len(homes)
a, b = len(homes), len(stores)
dist_arr = [[0] * b for _ in range(a)]
for i in range(a):
    x1, y1 = homes[i]
    for j in range(b):
        x2, y2 = stores[j]
        dist_arr[i][j] = abs(x1 - x2) + abs(y1 - y2)
closed = [0] * b
dfs(0, 0)
print(ans)


