import sys
from collections import defaultdict
sys.stdin = open('input.txt')

n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))
# index i까지의 누적합을 m으로 나눈 나머지를 저장할 공간 remainder
# 같은 나머지가 나오는 idx의 갯수를 remainder에 저장한다
# 아무것도 선택하지 않았을 때인 0은 따로 추가
remainder = defaultdict(int)
remainder[0] += 1
for i in range(1, n+1):
    nums[i] += nums[i-1]
    remainder[nums[i]%m] += 1

ans = 0
# 같은 나머지가 나오는 idx를 2개 고르면 그 구간의 누적합은 m의 배수가 된다
for key in remainder:
    k = remainder[key]
    ans += k * (k-1) // 2

print(ans)



