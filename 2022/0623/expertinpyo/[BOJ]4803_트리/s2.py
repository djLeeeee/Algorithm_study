# 메모리초과 방지 dfs
from sys import setrecursionlimit as st
st(10 ** 6)

def dfs(x):
    global tree
    visited[x] = 1
    for new_x in arr[x]:
        if not visited[new_x]:
            if connected[x][new_x]:
                tree = False
            else:
                connected[x][new_x] = 1
                connected[new_x][x] = 1
            dfs(x)
tc = 0
while True:
    n, m = map(int, input().split())
    if not n and not m:
        break
    tc += 1
    arr = [[] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    cnt = 0
    connected = [[0] * (n + 1) for _ in range(n+1)]
    visited = [0] * (n+1)
    for i in range(1, n+1):
        tree = True
        if not visited[i]:
            dfs(i)
            if tree:
                cnt += 1

    if not cnt:
        print(f'Case {tc}: No trees.')
    else:
        if cnt == 1:
            print(f'Case {tc}: There is one tree.')
        else:
            print(f'Case {tc}: A forest of {cnt} trees.')