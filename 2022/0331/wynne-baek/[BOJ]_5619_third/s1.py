import sys
import heapq
sys.stdin = open('input.txt')

def solution(N):
    for i in range(N):
        for j in range(N):
            if i != j:
                num = nums[i] + nums[j]
                if len(result) <= 3 or int(num) < result[2]:
                    heapq.heappush(result, int(num))
                elif len(result) == 3 and int(num) > result[2]:
                    break
    heapq.heappop(result)
    heapq.heappop(result)
    return result[0]

N = int(sys.stdin.readline())
nums = []
result = []
heapq.heapify(result)
for _ in range(N):
    nums.append(sys.stdin.readline().strip())
nums = tuple(sorted(nums))
if N == 3:
    print(solution(3))
elif N > 3:
    print(solution(N))