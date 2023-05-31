# https://www.acmicpc.net/problem/2812'
import sys
sys.stdin = open("./input/2812.txt")
input = sys.stdin.readline
# ----------------------------------------

N, K = map(int, input().split())
nums = input().rstrip()
stack = []

for n in nums:
    while stack and K and stack[-1] < n:
        stack.pop()
        K -= 1
    stack.append(n)

answer = stack[:-K] if K else stack
print("".join(answer))