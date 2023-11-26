# 백준 1507번 궁금한 민호

import sys
sys.stdin = open('input.txt')

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
road = [[1] * n for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if k != a and k != b and a != b:
                # 도로가 이어지지 않아도 최단거리라면 도로 없애기
                if data[a][b] == data[a][k] + data[k][b]:
                    road[a][b] = 0
                # input으로 주어진 도로가 최단거리가 아닐때(?)
                elif data[a][b] > data[a][k] + data[k][b]:
                    print(-1)
                    sys.exit()

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if road[i][j]:
            ans += data[i][j]
print(ans)