# 탑
# https://www.acmicpc.net/problem/2493
import sys
sys.stdin = open("./input/quiz3.txt")
input = sys.stdin.readline
# ----------------------------------------
def solution():
    N = int(input())
    towers = list(map(int, input().split()))

    stk = []
    answer = []

    for idx in range(1, N + 1):
        tower = towers[idx - 1]
        
        while stk and stk[-1][0] <= tower:
            stk.pop()

        if len(stk) == 0:
            answer.append(0)
            stk.append([tower, idx])
            
        else:
            answer.append(stk[-1][1])
            stk.append([tower, idx])
    return answer


# ----------------------------------------
for _ in range(int(input())):
    res = solution()
    print(*res)