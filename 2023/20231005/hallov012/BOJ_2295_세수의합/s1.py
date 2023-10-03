import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
nums = sorted([int(input()) for _ in range(n)])

# 두 수의 합을 저장
sum_set = set()
for a in nums:
    for b in nums:
        sum_set.add(a+b)

ans = set()
# a+b+c = d이고 d가 nums에 속해야 한다
# a+b = d-c
for d in nums:
    for c in nums:
        if (d-c) in sum_set:
            ans.add(d)

ans = sorted(list(ans), reverse=True)
print(ans[0])
