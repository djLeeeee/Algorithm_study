# 백준 11000번 강의실 배정

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

N = int(input())
schedule = []
for _ in range(N):
    s, t = map(int, input().split())
    schedule.append((s, t))
schedule.sort(key=lambda x : x[0])
end = []
heapq.heappush(end, schedule[0][1])
for i in range(1, N):
    if end[0] > schedule[i][0]:                 # 수업 시작 시간이 이전 수업 끝시간보다 빨리 시작한다면(수업 이어서 못함)
        heapq.heappush(end, schedule[i][1])     # 해당 수업 끝시간을 end에 넣음
    else:                                       # 수업을 이어서 진행할 수 있다면
        heapq.heappop(end)                      # 원래 수업 끝시간 빼내고
        heapq.heappush(end, schedule[i][1])     # 새 수업 끝시간으로 갱신
print(len(end))