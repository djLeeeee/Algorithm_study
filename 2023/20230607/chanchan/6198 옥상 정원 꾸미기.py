# https://www.acmicpc.net/problem/6198'
import sys
sys.stdin = open("./input/6198.txt")
input = sys.stdin.readline
# ----------------------------------------

N = int(input())
nums = [int(input()) for _ in range(N)]
stk = []
ans = 0

for n in nums:
    while stk and stk[-1] <= n:
        stk.pop()
    stk.append(n)

    ans += len(stk) - 1

print(ans)
