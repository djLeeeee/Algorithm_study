import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
data.sort()

que = []
for deadLine, cnt in data:
    heapq.heappush(que, cnt)
    if deadLine < len(que):
        heapq.heappop(que)

print(sum(que))