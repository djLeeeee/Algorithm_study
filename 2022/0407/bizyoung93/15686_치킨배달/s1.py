from itertools import combinations
import sys

sys.stdin = open('input.txt')


def do(open):
    global ans
    total = 0
    for r in range(H):
        min_value = 12345
        for c in open:
            if g[r][c] < min_value:
                min_value = g[r][c]
        total += min_value
        # 중간에 값을 넘어버리면 더 계산하지 않고 중단
        if total > ans:
            return
    if total < ans:
        ans = total


# 폐업시키지 않을 치킨집을 최대 M개
N, M = map(int, input().split())
house_list = []
chicken_list = []

# 치킨집과 집 좌표를 넣어준다.
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            house_list.append((i, j))
        elif temp[j] == 2:
            chicken_list.append((i, j))

# 2차원 배열을 만드는 데 세로는 집의 개수, 가로는 가게의 개수
H = len(house_list)
C = len(chicken_list)
g = []
for i in range(H):
    temp = []
    for j in range(C):
        # 각 집으로부터 치킨집까지의 거리를 계산한 후, 그 중 살린 가게들로의 거리 중 가장 가까운 곳을 잡으려 한다.
        temp.append(abs(house_list[i][0]-chicken_list[j][0]) + abs(house_list[i][1]-chicken_list[j][1]))
    g.append(temp)

ans = N * N * N

open_list = tuple(combinations(range(C), M)) # 살릴 가게들의 조합
for open in open_list:
    do(open)
print(ans)
