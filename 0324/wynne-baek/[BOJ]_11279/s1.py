import heapq
import sys
sys.stdin = open('input.txt')

# heapq.heapify(my_list) # my_list를 힙 구조로 변경
# heapq.heappush(my_list, my_num) # 힙 my_list에 원소 my_num 추가
# x = heapq.heappop(my_list) # 힙 my_list에서 최솟값을 뽑아 x에 저장

N = int(sys.stdin.readline())
max_heap = []
heapq.heapify(max_heap)
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0 :
        if not max_heap:
            print(0)
        else:
            print(heapq.heappop(max_heap)[1])
    else:
        heapq.heappush(max_heap, (-x, x))