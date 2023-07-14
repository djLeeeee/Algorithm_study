# 최소 강의실 => 모든 수업 가능하게
import heapq
N = int(input())
dic = dict()
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort(key= lambda x:x[0])
start, end = float("inf"), -1
for a, b in arr:
    start, end = min(start, a), max(end, b)
can_go = [[] for _ in range(b)]
for a, b in arr:
    can_go[a].append(b)

heap = []
for i in can_go[start]:
    heapq.heappush(heap, (1, start, i))
while heap:
    cnt, fr, to = heapq.heappop(heap)
    if to == end:
        print(cnt)
        exit()
    if len(can_go[to]):
        for i in can_go[to]:
            heapq.heappush(heap, (cnt+1, to, i))
