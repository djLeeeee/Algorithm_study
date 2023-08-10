# 사이클 존재 여부 판단

from collections import deque
def bfs(x):
    queue = deque([x])
    tree = True
    while queue:
        x = queue.popleft()
        if visited[x]:
            tree = False
        else:
            visited[x] = 1
        for new_x in arr[x]:
            if not visited[new_x]:
                queue.append(new_x)
    return tree

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
    visited = [0] * (n+1)
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            if bfs(i):
                cnt += 1

    if not cnt:
        print(f'Case {tc}: No trees.')
    else:
        if cnt == 1:
            print(f'Case {tc}: There is one tree.')
        else:
            print(f'Case {tc}: A forest of {cnt} trees.')