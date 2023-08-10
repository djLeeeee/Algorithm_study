import sys, collections, heapq

input = sys.stdin.readline

N, L = map(int, input().strip().split())

my_list = list(map(int, input().strip().split()))

Q = collections.deque([])

heap = []

for i in range(N):
    check_v = my_list[i]
    Q.append(check_v)
    heapq.heappush(heap, check_v)
    if i >= L:
        check_v2 = Q.popleft()
        if check_v2 == heap[0]:
            heapq.heappop(heap)
    print(heap[0], end=' ')

