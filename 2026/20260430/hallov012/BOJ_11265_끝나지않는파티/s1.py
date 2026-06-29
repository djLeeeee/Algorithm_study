import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for _ in range(m):
    a, b, c = map(int, input().split())
    if dist[a-1][b-1] > c:
        print("Stay here")
    else:
        print("Enjoy other party")