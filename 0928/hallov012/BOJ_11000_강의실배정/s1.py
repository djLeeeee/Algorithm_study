import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(classes, (s, e))
rooms = []
# 제일 빨리 시작하는 강의의 종료 시간 넣기
heapq.heappush(rooms, heapq.heappop(classes)[1])
while classes:
    s, e = heapq.heappop(classes)
    # 제일 빨리 비는 강의실에 들어갈 수 있다면 거기서 강의 시작
    if s >= rooms[0]:
        heapq.heappop(rooms)
        heapq.heappush(rooms, e)
    # 제일 빨리 비는 강의실에 들어갈 수 없다면 새로운 강의실
    else:
        heapq.heappush(rooms, e)
print(len(rooms))