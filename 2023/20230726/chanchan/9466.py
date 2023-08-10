# https://www.acmicpc.net/problem/9466
import sys
from collections import deque
sys.stdin = open("./input/9466.txt")
input = sys.stdin.readline

# ----------------------------------------


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x) #사이클을 이루는 팀을 확인하기 위함
    number = numbers[x]
    
    if visited[number]: #방문가능한 곳이 끝났는지
        if number in cycle: #사이클 가능 여부
            result += cycle[cycle.index(number):] #사이클 되는 구간 부터만 팀을 이룸
        return
    else:
        dfs(number)
=======
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
