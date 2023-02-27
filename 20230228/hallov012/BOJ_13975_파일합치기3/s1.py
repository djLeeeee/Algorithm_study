import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    arr = list(map(int, input().split()))
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
    ans = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        ans += a+b
        heapq.heappush(heap, a+b)
    print(ans)

