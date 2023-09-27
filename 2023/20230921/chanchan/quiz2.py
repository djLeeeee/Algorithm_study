# 두 배열의 합
# https://www.acmicpc.net/problem/2143'
import sys
sys.stdin = open("./input/quiz2.txt")
input = sys.stdin.readline
# ----------------------------------------
goal = int(input())
ans = 0
sums = {}

N = int(input())
N_arr = list(map(int, input().split()))

M = int(input())
M_arr = list(map(int, input().split()))

for i in range(N):
    for j in range(i + 1, N + 1):
        temp = sum(N_arr[i: j])
        sums[temp] = sums.get(temp, 0) + 1

for i in range(M):
    for j in range(i + 1, M + 1):
        
        temp = sum(M_arr[i: j])
        ans += sums.get(goal - temp, 0)
        
print(ans)
