# https://www.acmicpc.net/problem/7983
import sys
sys.stdin = open("./input/7983.txt")
input = sys.stdin.readline
# ----------------------------------------

N = int(input())

assignments = []
for _ in range(N):
    assignments.append(list(map(int, input().split())))
assignments.sort(key=lambda x: x[1], reverse=True)

days = assignments[0][1]
for n in range(N):
    # assignments[n] = ([0] = 필요한 시간, [1] = 마감일)
    days = min(days, assignments[n][1]) - assignments[n][0]

print(days)
