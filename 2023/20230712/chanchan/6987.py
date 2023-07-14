# https://www.acmicpc.net/problem/6987
import sys
input = sys.stdin.readline
sys.stdin = open("./input/6987.txt")
# ----------------------------------------

# 팀의 게임 수가 5회인지 체크
def cond1(records):
    for i in range(0, 18, 3):
        if sum(records[i:i+3]) != MAX_GAME_CNT:
            return False
    return True

# 팀들의 기록에서 승 수의 합과 패배 수의 합이 같은지
def cond2(records):
    win, lose = 0, 0
    for i in range(0, 18, 3):
        win += records[i]
        lose += records[i+2]
    return win == lose

# 무승부의 수가 이상한지 아닌지 체크
def cond3(records):
    cnt = 0
    for i in range(1, 18, 3):
        cnt  = abs(cnt - records[i])
    return cnt == 0

MAX_GAME_CNT = 5
board = [list(map(int, input().split())) for _ in range(4)]

result = []
for ind in range(4):
    case = board[ind]
    conditions = [cond1, cond2, cond3]
    for cond in conditions:
        if (not cond(case)):
            result.append(0)
            break
    else:
        result.append(1)

print(*result)
    
