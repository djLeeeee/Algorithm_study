"""플로이드 와샬만 생각나서 구글링!"""

import sys
sys.stdin = open('input.txt')

def dfs(start, exist, result):
    for s, e in exist[start]:
        if result[s] == 0:
            result[s] = result[start] + e
            dfs(s, exist, result)
    return

V = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(V)]
exist = [[] for _ in range(V+1)]
for i in range(V):
    for j in range(1, len(arr[i])//2):
        exist[arr[i][0]].append([arr[i][j*2-1], arr[i][j*2]])

result1 = [0 for _ in range(V+1)]
dfs(1, exist, result1)
result1[1] = 0
tempmax = 0
index = 0

for i in range(len(result1)):
    if tempmax < result1[i]:
        tempmax = result1[i]
        index = i

result2 = [0 for _ in range(V+1)]
dfs(index, exist, result2)
result2[index] = 0
print(max(result2))