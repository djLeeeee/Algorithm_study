# https://www.acmicpc.net/problem/9466
import sys
from collections import deque
sys.stdin = open("./input/9466.txt")
input = sys.stdin.readline
sys.setrecursionlimit(sys.maxsize)
# ----------------------------------------



def dfs(n: int, team_members:list, group:list):
    checked[n] = True
    group.append(n)
    num = nums[n]
    
    if checked[num]:
        if num in group:
            for member in group[group.index(num):]:
                team_members.append(member)
        return
    else:
        dfs(num, team_members, group)


for _ in range(int(input())):
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    checked = [1] + [0] * N
    team_members = []

    for i in range(1, N + 1):
        if not checked[i]:
            group = []
            dfs(i, team_members, group)
            
    print(N - len(team_members)) #팀에 없는 사람 수