import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
min_heap, max_heap = [], []
prob_dict = defaultdict(int)
for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(min_heap, (l, p))
    heapq.heappush(max_heap, (-l, -p))
    prob_dict[p] = l

m = int(input())
for _ in range(m):
    command = input().split()
    if command[0] == 'add':
        p, l = int(command[1]), int(command[2])
        heapq.heappush(min_heap, (l, p))
        heapq.heappush(max_heap, (-l, -p))
        prob_dict[p] = l
    elif command[0] == 'solved':
        p = int(command[1])
        prob_dict[p] = 0
    elif command[0] == 'recommend':
        x = int(command[1])
        if x == 1:
            while max_heap:
                l, p = max_heap[0]
                p *= -1
                l *= -1
                if prob_dict[p] == l:
                    print(p)
                    break
                else:
                    heapq.heappop(max_heap)
        else:
            while min_heap:
                l, p = min_heap[0]
                if prob_dict[p] == l:
                    print(p)
                    break
                else:
                    heapq.heappop(min_heap)