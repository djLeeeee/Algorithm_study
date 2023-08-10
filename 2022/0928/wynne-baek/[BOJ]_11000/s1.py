import sys
import heapq
sys.stdin = open('input.txt')

classes = []
N = int(input())
for _ in range(N):
    start, end = map(int, input().split())
    classes.append([start, end])

classes.sort()

classroom = []
heapq.heappush(classroom, classes[0][1])

for i in range(1, N):
    if classes[i][0] < classroom[0]:
        heapq.heappush(classroom, classes[i][1])
    else:
        heapq.heappop(classroom)
        heapq.heappush(classroom, classes[i][1])

print(len(classroom))