import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

sum_set = set()
for a in nums:
    for b in nums:
        sum_set.add(a + b)

ans = 0
for c in nums:
    for d in nums:
        # a + b + c = d
        # a + b = d - c
        if (d - c) in sum_set:
            ans = max(ans, d)

print(ans)