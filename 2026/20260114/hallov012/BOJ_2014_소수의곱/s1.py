import sys, heapq
sys.stdin = open('input.txt')

k, n = map(int, input().split())
nums = list(map(int, input().split()))

q = []
for idx, num in enumerate(nums):
    heapq.heappush(q, (num, idx))

min_num = 0
for _ in range(n-1):
    a_num, a_idx = heapq.heappop(q)
    for b_idx, b_num in enumerate(nums):
        # 같은 수 여러번 넣는거 방지
        if b_idx > a_idx:
            break
        heapq.heappush(q, ((a_num * b_num, b_idx)))

print(heapq.heappop(q)[0])