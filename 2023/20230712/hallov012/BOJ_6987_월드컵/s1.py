import sys
from itertools import combinations
sys.stdin = open('input.txt')

def find(idx):
    global flag
    if idx == n:
        for team in teams:
            if sum(team):
                break
        else:
            flag = True
        return
    a, b = games[idx]
    for x, y in case:
        if teams[a][x] and teams[b][y]:
            teams[a][x] -= 1
            teams[b][y] -= 1
            find(idx+1)
            teams[a][x] += 1
            teams[b][y] += 1

input = sys.stdin.readline

ans = []
games = list(combinations(range(6), 2))
n = len(games)
# 경기의 결과 팀 두개를 기준으로 승, 패/ 무, 무/ 패, 승
case = [(0, 2), (1, 1), (2, 0)]

for _ in range(4):
    line = list(map(int, input().split()))
    teams = []
    for i in range(1, 7):
        teams.append(line[3*(i-1): 3*i])
    flag = False
    find(0)
    if flag:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)
