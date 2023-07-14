# https://www.acmicpc.net/problem/13164
import sys
sys.stdin = open("./input/13164.txt")
input = sys.stdin.readline
# ----------------------------------------
N, K = map(int, input().split())

heights = list(map(int, input().split()))
gaps = []
for i in range(N - 1):
    gaps.append(heights[i + 1] - heights[i])

gaps.sort()
print(sum(gaps[:N - K]))