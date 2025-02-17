import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
c_lst = [sorted(list(map(int, input().split())), reverse=True) for _ in range(n)]

que = []
min_s = sys.maxsize
max_s = 0

for i in range(n):
    s = c_lst[i].pop()
    min_s = min(min_s, s)
    max_s = max(max_s, s)
    heapq.heappush(que, (s, i))

ans = max_s - min_s

while que:
    min_q, idx = heapq.heappop(que)
    if not c_lst[idx]:
        break
    s = c_lst[idx].pop()
    heapq.heappush(que, (s, idx))

    max_s = max(max_s, s)
    min_s = que[0][0]
    ans = min(ans, max_s - min_s)

print(ans)
