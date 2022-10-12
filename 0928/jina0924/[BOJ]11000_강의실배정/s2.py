# 백준 11000번 강의실 배정 - 시간초과

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq


N = int(input())
schedule = []
for _ in range(N):
    s, t = map(int, input().split())
    heapq.heappush(schedule, (t, s))
cnt = 0
while schedule:
    end = heapq.heappop(schedule)[0]
    for cls in schedule:
        if cls[1] >= end:
            end = cls[0]
            schedule.remove(cls)
    cnt += 1
print(cnt)