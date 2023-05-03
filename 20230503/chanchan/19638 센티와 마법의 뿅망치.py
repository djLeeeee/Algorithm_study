# https://www.acmicpc.net/problem/19638
import heapq
import sys
sys.stdin = open("./input/19638.txt")
input = sys.stdin.readline

N, H, T = map(int, input().split())
cnt = 0
"""
heapq는 기본적으로 최소힙을 기준으로 만들어져 있기 때문에
각각의 값에 (-1)을 곱하여 최대힙을 구현했습니다.
"""
heights = [int(input()) * (-1) for _ in range(N)]
heapq.heapify(heights)

def is_able_to_hit(T, H, heights, cnt):
    height = (-1) * heights[0]
    cond1 = T > cnt
    cond2 = height >= H
    cond3 = height != 1
    return (cond1 and cond2 and cond3)

while is_able_to_hit(T, H, heights, cnt):
    before_height = (-1) * heapq.heappop(heights)
    after_height = before_height // 2
    heapq.heappush(heights, after_height * (-1))
    cnt += 1

if heights[0] * (-1) >= H:
    print("NO")
    print(heights[0] * (-1))
else:
    print("YES")
    print(cnt)