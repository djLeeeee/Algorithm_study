import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

def bfs(arr):
    check = [0] * (n+1)
    que = deque([arr[0]])
    check[arr[0]] = 1
    temp = 0
    cnt = 1
    while que:
        x = que.popleft()
        temp += population[x]
        for y in g[x]:
            if not check[y] and y in arr:
                check[y] = 1
                cnt += 1
                que.append(y)
    if cnt == len(arr):
        return temp
    return False

def dfs(num, cnt):
    global ans
    if cnt == num:
        arr_1 = []
        arr_2 = []
        for i in range(1, n+1):
            if visited[i]:
                arr_1.append(i)
            else:
                arr_2.append(i)
        temp_1, temp_2 = bfs(arr_1), bfs(arr_2)
        if temp_1 and temp_2:
            ans = min(ans, abs(temp_1-temp_2))
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = 1
            dfs(num, cnt+1)
            visited[i] = 0

input = sys.stdin.readline

n = int(input())
population = [0] + list(map(int, input().split()))
g = defaultdict(list)
for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, row[0]+1):
        g[i].append(row[j])

ans = sys.maxsize
# 1번이 선택하게 되는 지역 수
for i in range(1, n//2+1):
    visited = [0] * (n+1)
    dfs(i, 0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
