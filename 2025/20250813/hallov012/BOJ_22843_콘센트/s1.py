import sys, heapq
sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
heap = [0] * m
# 빨리 끝나는 시간에 추가하기
for t in arr:
    c = heapq.heappop(heap)
    heapq.heappush(heap, t+c)
print(max(heap))
