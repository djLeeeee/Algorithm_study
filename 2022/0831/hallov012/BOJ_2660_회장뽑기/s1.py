"""
플로이드 와샬을 이용한 문제 풀이
플로이드 와샬: 모든 정점에서 모든 정점으로의 최단거리를 구하는 알고리즘
"""
import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
dist = [[sys.maxsize] * (n+1) for _ in range(n+1)]
# 자신과 자신 사이의 거리는 0
for i in range(1, n+1):
    dist[i][i] = 0

# 친구관계라면 dist는 1로 표현
while True:
    a, b = map(int, input().split())
    if (a, b) == (-1, -1):
        break
    dist[a][b] = 1
    dist[b][a] = 1

# i와 j 사이에 k라는 중간지점이 있는지 조회
# 현재 i => j의 거리와 i => j => k를 조회해 더 작은 값으로 dist를 갱신
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[j][k])

ans = sys.maxsize
candidate = []
for i in range(1, n+1):
    if ans > max(dist[i][1:]):
        ans = max(dist[i][1:])
        candidate = [i]
    elif ans == max(dist[i][1:]):
        candidate.append(i)

print(ans, len(candidate))
print(*candidate)
