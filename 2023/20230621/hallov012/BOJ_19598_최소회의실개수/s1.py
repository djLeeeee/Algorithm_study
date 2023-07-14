import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting.sort()
q = [0]
for s, e in meeting:
    t = heapq.heappop(q)
    if t <= s:
        heapq.heappush(q, e)
    else:
        heapq.heappush(q, t)
        heapq.heappush(q, e)
print(len(q))

