# 백준 19598번 최소 회의실 개수

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

N = int(input())
meetings = sorted(tuple(map(int, input().split())) for _ in range(N))   # 회의 시작 시간 순으로 정렬
room = [(meetings[0][1], meetings[0][0])]       # 회의 끝나는 시간대로 heap정렬하기 위해 순서 바꿔 넣음
for i in range(1, N):
    s2, e2 = meetings[i]
    e1, s1 = heapq.heappop(room)
    if e1 > s2:                                 # 제일 먼저 끝나는 회의보다 현재 살펴보는 회의가 일찍 시작한다면 회의실 += 1
        heapq.heappush(room, (e1, s1))
    heapq.heappush(room, (e2, s2))
print(len(room))