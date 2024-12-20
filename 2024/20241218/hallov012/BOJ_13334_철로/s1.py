import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
employees = [sorted(list(map(int, input().split()))) for _ in range(n)]
employees.sort(key=lambda x: (x[1], x[0]))
d = int(input())

que = []
ans = 0

for s, e in employees:
    heapq.heappush(que, s)
    d_start = e - d
    while que and que[0] < d_start:
        heapq.heappop(que)
    ans = max(ans, len(que))

print(ans)