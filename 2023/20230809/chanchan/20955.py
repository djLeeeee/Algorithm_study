# https://www.acmicpc.net/problem/20955
import sys
sys.stdin = open("./input/20955.txt")
input = sys.stdin.readline
# ----------------------------------------
def find(parent, u):
    if parent[u] != u:
        return find(parent, parent[u])
    return u

def union(parent, u, v):
    u, v = sorted([find(parent, u), find(parent, v)])
    parent[v] = u
# ----------------------------------------
# 학생아 왜 그랬어... 졸다가 머가리가 깨지니...
# 그리고 문제야 넌 나한테 왜 그래
# ----------------------------------------
N, M = map(int, input().split()) # 뉴런, 시냅스
parent = list(range(N + 1))
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    if find(parent, u) == find(parent, v):
        cnt += 1
    union(parent, u, v)

link = 0
for i in range(1, N):
    if find(parent, i) != find(parent, i + 1):
        union(parent, i, i + 1)
        link += 1

print(cnt + link)
    