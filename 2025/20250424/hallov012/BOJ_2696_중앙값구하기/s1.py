import sys, heapq
sys.stdin = open('input.txt')

def get_rows(length):
    rows = length // 10
    if length % 10:
        rows += 1
    return rows

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    m = int(input())
    rows = get_rows(m)
    nums = []
    for _ in range(rows):
        rows = list(map(int, input().split()))
        nums = nums + rows

    left, right, ans = [], [], [nums[0]]
    mid = nums[0]
    for i, num in enumerate(nums[1:]):
        if num < mid:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)
        if i % 2:
            if len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)
            elif len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            ans.append(mid)

    print(len(ans))
    rows = get_rows(len(ans))
    for i in range(rows):
        if i != rows-1:
            print(*ans[i*10: (i+1)*10])
        else:
            print(*ans[i*10:])