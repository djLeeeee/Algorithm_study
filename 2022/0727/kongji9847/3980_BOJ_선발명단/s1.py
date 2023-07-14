# dfs 완전 탐색
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 1. dfs로 완전탐색
player_list = {0: 'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k'}

def dfs(position, players, ability_sum):
    global best

    # 종료조건 - 모든 포지션에 선수를 정했을 때
    if position >= 11:
        best = max(best, ability_sum)
        #print(ability_sum, players)
        return

    # 진행 - 해당 포지션에 player를 넣고 다음 단계로 넘어가기
    for i in range(11):
        if data[i][position] and player_list[i] not in players:
            dfs(position+1, players+player_list[i], ability_sum+data[i][position])


# 0. input 받기
T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(11)]
    best = 0
    dfs(0, '', 0)
    print(best)