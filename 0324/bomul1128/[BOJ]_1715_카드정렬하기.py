from sys import stdin as s
import heapq

input = s.readline

n = int(input())
my_list = [int(input()) for _ in range(n)]
heapq.heapify(my_list)
result = 0
for i in range(n - 1):
    x = heapq.heappop(my_list)
    y = heapq.heappop(my_list)
    result += x + y
    heapq.heappush(my_list, x + y)
print(result)
