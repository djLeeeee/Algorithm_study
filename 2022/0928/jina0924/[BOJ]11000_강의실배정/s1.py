# 백준 11000번 강의실 배정 - 시간초과

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
schedule = []
for _ in range(N):
    s, t = map(int, input().split())
    schedule.append((s, t))
schedule.sort(key=lambda x: x[1])
cnt = 0
while schedule:
    end = schedule.pop(0)[1]
    for cls in schedule:
        if cls[0] >= end:
            end = cls[1]
            schedule.remove(cls)
    cnt += 1
print(cnt)