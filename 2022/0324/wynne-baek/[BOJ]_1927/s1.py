import heapq
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())       # 처음엔 그냥 input() 썼는데, 시간초과 떴음!
my_list = []
heapq.heapify(my_list)
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if my_list:
            print(heapq.heappop(my_list))
        else:
            print(0)
    else:
        heapq.heappush(my_list, x)
