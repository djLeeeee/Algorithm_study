# https://www.acmicpc.net/problem/2610'
import sys
sys.stdin = open("./input/2610.txt")
input = sys.stdin.readline
from collections import deque
# ----------------------------------------
N = int(input())
K = int(input())
leaders = []
dist = [[sys.maxsize] * (N + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    dist[n][n] = 0

for _ in range(K):
    n1, n2 = map(int, input().split())
    dist[n1][n2] = dist[n2][n1] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k], dist[k][j])

vst = [0] * (N + 1)
network = []
ans =0 
for i in range(1, N + 1):
    if not vst[i]:
       ans += 1
       vst[i] = 1
       network.append(i)
       for j in range(1, N + 1):
           if dist[i][j] != sys.maxsize and i != j:
               network.append(j)
               vst[j] = 1
        leaders.append(getLeader(network)) 