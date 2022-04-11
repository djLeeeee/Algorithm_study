from itertools import combinations
import sys
sys.stdin = open('input.txt')

def how_far():
    distance = 0
    for x, y in houses:
        temp = 10000
        for j, k in new_chicken:
            dist = abs(x-j) + abs(y-k)
            if dist < temp:
                temp = dist
        distance += temp
    result.append(distance)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for __ in range(N)]
houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))
nCm = combinations(chickens, M)
result = []
for new_chicken in nCm:
    how_far()
print(min(result))
