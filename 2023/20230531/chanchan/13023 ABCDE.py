# https://www.acmicpc.net/problem/13023
import sys
sys.stdin = open("./input/13023.txt")
input = sys.stdin.readline
# ----------------------------------------
N, M = map(int, input().split())

edges = [[] for _ in range(N)]
answer = 0

def dfs(num, vst, cnt):
    global answer
    if answer: # 이거 없으면 시간 초과
        print(answer)
        exit()
        
    if cnt == 5:
        answer = 1
        return
    
    for next in edges[num]:
        if not vst[next]:
            vst[next] = 1
            dfs(next, vst, cnt + 1)
            vst[next] = 0

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

vst = [0] * N
for n in range(N):
    vst[n] = 1
    dfs(n, vst, 1)
    vst[n] = 0

print(answer)